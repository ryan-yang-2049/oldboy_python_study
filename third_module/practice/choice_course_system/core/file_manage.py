
import os
import sys
import pickle
if os.name == 'posix':
    default_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'+'database'+'/'
elif os.name == 'nt':
    default_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\'+'database'+'\\'


school_dict = {
    'BJ':{'school_name':'oldboy_bj',
          'course_info':{'python':{'course_price':5000,'course_period':4},'linux':{'course_price':3000,'course_period':2}},
          'class_info':{'B1':'python','B2':'linux','B3':'python'},
          'teacher_info':{
              'alex':{'course_name':'python','salary':10000,'class_name':'B1'},

          },
          'student_info':{'ryan':{'B2':'linux'},'ryan1':{'B1':'python'},'ryan2':{'B1':'python'},'ryan3':{'B1':'python'},'ryan4':{'B1':'python'},

                          'cherry':{'B2':'linux'},'cherry1': {'B2':'linux'},'cherry2': {'B2':'linux'},'cherry3': {'B2':'linux'},'cherry4': {'B2':'linux'},
                          },
          },


    'SH': {'school_name': 'oldboy_sh',
           'course_info': {'go': {'course_price': 6000, 'course_period': 5}},
           'class_info': {'S1': 'go', 'S2': 'go',},
           'teacher_info': {'egon': {'course_name': 'go', 'salary': 10000, 'class_name':'S1'}},
                     'student_info':{'ryan5':{'S1':'GO'},'ryan6':{'S2':'GO'},
                          'cherry5': {'S1':'GO'},'cherry6': {'S2':'GO'},
                          },
           },

}

user_dict = {
    'admin':{'admin':{'role':'admin','passwd':'1234','login_statsu':0}},
    'teacher':{
        'alex':{'role':'teacher','passwd':'1234','login_status':0},
        'egon':{'role':'teacher','passwd':'1234','login_status':0},
    },

    'student':{
        'ryan':{'role':'student','passwd':'1234','login_status':0},
        'ryan1':{'role':'student','passwd':'1234','login_status':0},
        'ryan2':{'role':'student','passwd':'1234','login_status':0},
        'ryan3':{'role':'student','passwd':'1234','login_status':0},
        'ryan4':{'role':'student','passwd':'1234','login_status':0},
        'ryan5':{'role':'student','passwd':'1234','login_status':0},
        'ryan6':{'role':'student','passwd':'1234','login_status':0},

        'cherry':{'role':'student','passwd':'1234','login_status':0},
        'cherry1':{'role':'student','passwd':'1234','login_status':0},
        'cherry2':{'role':'student','passwd':'1234','login_status':0},
        'cherry3':{'role':'student','passwd':'1234','login_status':0},
        'cherry4':{'role':'student','passwd':'1234','login_status':0},
        'cherry5':{'role':'student','passwd':'1234','login_status':0},
        'cherry6':{'role':'student','passwd':'1234','login_status':0},
}}

'''创建数据文件信息'''
def file_operate(filename,mode,dirname=default_path,data=None):
    if mode == 'w':
        write_file = open("%s/%s.pkl"%(dirname,filename),'wb')
        pickle.dump(data,write_file)
        write_file.close()
        return True,"写入成功"
    elif mode == 'r':
        filename = "%s/%s.pkl" % (dirname, filename)
        # print(filename)
        if os.path.isfile(filename) and os.path.exists(filename):
            read_file = open(filename, 'rb')
            return_data = pickle.load(read_file)
            read_file.close()
            return return_data
        else:
            return None


# 用于初始化数据文件信息
# school_database = file_operate('school','w',data=school_dict)
# user_database = file_operate('userinfo','w',data=user_dict)

school_data = file_operate('school','r')
user_data = file_operate('userinfo','r')

