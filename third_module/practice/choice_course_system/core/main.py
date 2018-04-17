# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'yangyang'
__mtime__ = '2018.01.10'
"""

import os,sys
import shelve
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


from conf.create_role_info import UserRoleInfo
from core import file_manage
# from core.school import School


'''用于登录验证的装饰器'''
def role_auth(role):
    def decorator(func):
        def wrapper(*args, **kwargs):
            name = input("login:").strip()
            passwd = input("password:").strip()
            global username
            username = name
            user_obj = UserRoleInfo(name,passwd,role)
            res = user_obj.verification_user()
            # print("res", res)
            if res:
                res['login_status'] = 1
                # print("res1",res)
                return func()
            else:
                print("用户信息错误！")
        return wrapper
    return decorator

'''用于查询根据班级查找学生的递归函数'''
def recursive(dic,li,arg):
    for key in dic.keys():
        if type(dic[key]) == dict:
            for k,v in dic[key].items():
                if k == arg:
                    li.append(key)
                else:
                    recursive(dic[key],li,arg)

class View(object):
    def __init__(self):
        self.school_data = file_manage.school_data
        self.user_data  = file_manage.user_data


@role_auth(role='admin')
class ManageView(View):
    '''
    管理视图
    '''
    def __init__(self):
        super().__init__()
        self.run_manageview() #正式的时候开启


    def run_manageview(self):
        manage_dict = {'1':['创建课程','add_course'],
                       '2':['创建班级','add_class'],
                       '3':['创建讲师','add_teacher'],
                       '4':['查看课程','check_course'],
                       '5':['查看班级','check_class'],
                       '6':['查看讲师','check_teacher'],
                       '7':['退出程序','break']
        }
        while True:
            for key,val in (self.school_data).items():
                print("地区名：%s,学校名：%s ;" %(key,val['school_name']))
            choice_addr = input("请选择地区名称，退出（Q）:").strip()
            if choice_addr == 'Q':break
            if choice_addr in self.school_data:
                self.school_info = self.school_data[choice_addr]
                while True:
                    for key,val in manage_dict.items():
                        print("\033[31;0m %s:%s\033[0m"%(key.center(3),str(val[0]).center(8)))
                    operate_choice = input("请选择序号执行：").strip()
                    if operate_choice not in manage_dict:continue
                    if operate_choice == '7':
                        print("byebye！")
                        break
                    if hasattr(self,manage_dict[operate_choice][1]):
                        execute_func = getattr(self,manage_dict[operate_choice][1])
                        execute_func()

    def add_course(self):

        while True:
            course_name = input("请输入课程名称,退出（Q）：").strip()
            if course_name == 'Q':break
            if course_name in self.school_info['course_info']:
                print("课程已存在！")
                continue
            course_price = input("请输入课程价格：").strip()
            if not course_price.isdigit():continue
            course_period = input("请输入课程周期:").strip()
            if not course_period.isdigit():continue
            self.school_info['course_info'].update({course_name:{'course_price':course_price,'course_period':course_period}})
            file_manage.file_operate('school','w',data=self.school_data)
            choice = input("继续请回车，退出（Q）！")
            if choice == 'Q':
               break



    def add_class(self):
        while True:
            class_name = input("请输入班级名称，退出（Q）:").strip()
            if len(class_name) == 0: continue
            if class_name == 'Q':break
            class_name_course = input("请输入班级的课程：").strip()
            if len(class_name_course) == 0:continue
            self.school_info['class_info'].update({class_name:class_name_course})
            file_manage.file_operate('school','w',data=self.school_data)
            choice = input("继续请回车，退出（Q）！")
            if choice == 'Q':
               break

    def add_teacher(self):
        while True:
            print("此处创建的教师，改名教师还要去注册，否则无法登录教师视图")

            teacher_name = input("请输入教师姓名,退出（Q）:").strip()
            if len(teacher_name) == 0: continue
            if teacher_name == 'Q':break
            teach_course = input("授课名：").strip()
            if len(teach_course) == 0:continue
            if teach_course not in self.school_info['course_info']:
                print("课程不存在！")
                continue
            teacher_salary = input("薪资：").strip()
            if not teacher_salary.isdigit(): continue
            teach_class = input("班级名称：").strip()
            if len(teach_class) == 0:continue
            if teach_class not in self.school_info['class_info']:
                print("班级不存在，如需创建班级，请回到上一界面！")
                continue
            if self.school_info['class_info'][teach_class] != teach_course:
                print("该班级已被 %s 课程占用！"%(self.school_info['class_info'][teach_class]))

            self.school_info['teacher_info'].update({teacher_name:{'course_name':teach_course, 'salary':teacher_salary,'class_name':teach_class}})
            file_manage.file_operate('school','w',data=self.school_data)
            choice = input("继续请回车，退出（Q）！")
            if choice == 'Q':
               break

    def check_course(self):
        '''
        'course_info':{'python':{'course_price':5000,'course_period':4},'Linux':{'course_price':5000,'course_period':4}}
        :return:
        '''
        print("\033[31;0m %s %s %s\033[0m"%('课程名'.center(5),'课程价格'.center(5),'课程周期'.center(5)))
        for key,val in (self.school_info['course_info']).items():
            # print(key,val['course_price'],val['course_period'])
            print("\033[31;0m %s %s %s \033[0m" % (key.center(8),str(val['course_price']).center(8),str(val['course_period']).center(8)))

        print("退出查看课程！")

    def check_class(self):
        '''
        'class_info':{'B1':'python','B2':'linux','B3':'python'}
        :return:
        '''
        print("\033[31;0m %s %s \033[0m" % ('班级名称'.center(5), '班级课程'.center(5)))
        for key,val in (self.school_info['class_info']).items():
            print("\033[31;0m %s %s  \033[0m" % (key.center(8),val.center(8) ))
        print("退出查看班级信息！")

    def check_teacher(self):
        '''
        'teacher_info':{'teacher_name1':{'password':'password','course_name':'python','salary':10000,'class_name':['B1','B2']}},
        :return:
        '''
        print("\033[31;0m %s %s %s %s \033[0m" % ('教师名称'.center(5), '授课名称'.center(5),'薪资'.center(5),'授课班级'))
        for key,val in (self.school_info['teacher_info']).items():
            print("\033[31;0m %s %s %s %s  \033[0m" % (key.center(8), val['course_name'].center(8),str(val['salary']).center(8),val['class_name']))
        print("退出教师查看！")


@role_auth(role='student')
class StudentView(View):
    '''学生视图'''
    def __init__(self):
        super().__init__()
        self.run_studentview()

    def run_studentview(self):
        while True:
            print("\033[31;0m 帮助有志向的年轻人通过努力获得体面的生活！ \033[0m")
            for key,val in (self.school_data).items():
                print("地区名：%s,学校名：%s ;" %(key,val['school_name']))
            choice_addr = input("请选择地区名称，退出（Q）:").strip()
            if choice_addr == 'Q':break
            if choice_addr not in self.school_data:continue
            if choice_addr in self.school_data:
                self.school_info = self.school_data[choice_addr]


            while True:
                student_choice_dict = {
                    '1': ['查看个人课程信息', 'check_course_info'],
                    '2':['创建课程信息','create_coursse'],
                    '3':['查看所有课程','check_addr_course_info']
                }
                for key,val in (student_choice_dict).items():
                    print(key,val[0])
                choice =input("请输入序号选择,退出（Q）：").strip()
                if choice == 'Q':break
                if choice not in student_choice_dict:continue
                if hasattr(self,student_choice_dict[choice][1]):
                    execute_func = getattr(self,student_choice_dict[choice][1])
                    execute_func()

    def check_addr_course_info(self):
        print("\033[31;0m %s %s %s\033[0m" % ('课程名'.center(5), '课程价格'.center(5), '课程周期'.center(5)))
        for key, val in (self.school_info['course_info']).items():
            # print(key,val['course_price'],val['course_period'])
            print("\033[31;0m %s %s %s \033[0m" % (
            key.center(8), str(val['course_price']).center(8), str(val['course_period']).center(8)))

        print("退出查看课程！")

    def check_course_info(self):
        '''
        又遇到怎么把装饰器里面登陆认证的用户名传递过来
        先直接用 传入用户名查看吧。
        难道退出都是while True 的break退出？
        '''
        while True:
            username = input("请输入您的用户名,退出（Q）:").strip()
            if username == 'Q':break
            if username not in self.school_info['student_info']:
                print("该用户还未创建课程信息！")
                continue
            for key,val in (self.school_info['student_info'][username]).items():
                print("\033[31;0m 班级名称:%s 课程名称：%s \033[0m" % (key.center(5), val.center(5)))

            break


    def create_coursse(self):
        while True:
            student_name = input("\033[34;0m输入学生的姓名：\033[0m").strip()
            if student_name not in self.user_data['student']:
                print("该用户未注册，创建课程必须先注册！")
                break
            choice_course = input("请输入课程名：").strip()
            if choice_course not in self.school_info['course_info']:
                print("课程不存在")
                break
            else:
                course_price = input("课程价格为： %s RMB，学习周期为：%s 个月 ，购买（Y），退出（Q）:" %(self.school_info['course_info'][choice_course]['course_price'],self.school_info['course_info'][choice_course]['course_period'])).strip()
                if course_price != "Y":
                    print("你已放弃购买！")
                    break

                class_list = []
                for key,val in (self.school_info['class_info']).items():
                    # print(key,val)
                    if choice_course == val:
                        class_list.append(key)
                for info in class_list:print("可选班级名称为：",info)
                class_name = input("选择的班级名称为：").strip()
                if class_name not in class_list:break
                # self.school_info['student_info'].update({student_name:{class_name:choice_course}})
                self.school_info['student_info'][student_name][class_name]=choice_course

                if file_manage.file_operate('school','w',data=self.school_data):
                    break



@role_auth(role='teacher')
class TeacherView(View):
    '''教师视图'''
    def __init__(self):
        super().__init__()
        self.run_teacherview()

    def run_teacherview(self):
        while True:
            print("\033[31;0m 教师查询页面 \033[0m")
            for key,val in (self.school_data).items():
                print("地区名：%s,学校名：%s ;" %(key,val['school_name']))
            choice_addr = input("请选择地区名称，退出（Q）:").strip()
            if choice_addr == 'Q':break
            if choice_addr not in self.school_data:continue
            if choice_addr in self.school_data:
                self.school_info = self.school_data[choice_addr]

            while True:

                teacher_choice_dict = {
                    '1':['查看班级信息','check_class_info'],
                }

                for key,val in (teacher_choice_dict).items():
                    print(key,val[0])
                choice = input("请输入序号选择,退出（Q）：").strip()
                if choice == 'Q': break
                if choice not in teacher_choice_dict: continue
                if hasattr(self,teacher_choice_dict[choice][1]):
                    execute_func = getattr(self,teacher_choice_dict[choice][1])
                    execute_func()


    def check_class_info(self):
        while True:
            teacher_name = input("请输入教师名称,退出（Q）:").strip()
            if teacher_name == 'Q':break
            if teacher_name not in self.school_info['teacher_info']:
                print("教师还未开始授课")
                continue
            teach_course = self.school_info['teacher_info'][teacher_name]['course_name']
            teach_class = self.school_info['teacher_info'][teacher_name]['class_name']
            teach_student_list = []
            student_dict = self.school_info['student_info']
            recursive(student_dict,teach_student_list,teach_class)
            if len(teach_student_list) == 0:
                print("%s 即将开课" % teach_course)
            else:
                print("授课班级名称：%s，共 %s 名学生，学生名字为： %s "%(teach_class,len(teach_student_list),' '.join(teach_student_list)))


