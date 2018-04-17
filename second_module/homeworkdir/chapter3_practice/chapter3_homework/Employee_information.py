#!/usr/bin/env python
#coding:utf-8
'''
employee_info
staff_id,name,age,phone,dept,enroll_date
1,Alex Li,22,13651054608,IT,2013-04-01
2,Jack Wang,28,13451024608,HR,2015-01-07
3,Rain Wang,21,13451054608,IT,2017-04-01

需求：
1.可进行模糊查询，语法至少支持下面3种查询语法:
find name,age from staff_table where age > 22
find * from staff_table where dept = "IT"
find * from staff_table where enroll_date like "2013"

2.可创建新员工纪录，以phone做唯一键(即不允许表里有手机号重复的情况)，staff_id需自增
语法: add staff_table Alex Li,25,134435344,IT,2015-10-29

3.可删除指定员工信息纪录，输入员工id，即可删除
语法: del from staff_table where  id=3

4.可修改员工信息，语法如下:
UPDATE staff_table SET dept="Market" WHERE  dept="IT" 把所有dept=IT的纪录的dept改成Market
UPDATE staff_table SET age=25 WHERE  name="Alex Li"  把name=Alex Li的纪录的年龄改成25
5.以上每条语名执行完毕后，要显示这条语句影响了多少条纪录。 比如查询语句就显示查询出了多少条、修改语句就显示修改了多少条等
'''

def operate_statement(arg):
    if arg == '查询':
        print('''
find name,age from staff_table where age > 22
find * from staff_table where dept = "IT"
find * from staff_table where enroll_date like "2013"        
        ''')
    elif arg == '添加':
        print("add staff_table Alex Li,25,134435344,IT,2015-10-29")
    elif arg == "删除":
        print('del from staff_table where  id=3')
    elif arg == "修改":
        print('''
\033[34;1mUPDATE staff_table SET dept = Market WHERE  dept = IT\033[0m
\033[34;1mUPDATE staff_table SET age = 25 WHERE  name = Alex Li\033[0m ''')


def login():
    _name = 'ryan'
    _passwd = '1234'
    count = 0
    while count < 3:
        user = input("login:").strip()
        passwd = input("password:").strip()
        count += 1
        if user == _name and passwd == _passwd:
            return True
        else:
            print("信息有误！")


def check_employ(data):
    with open("employee_info", 'r', encoding='utf-8') as read_file:
        res = data.split(" ")
        for line in read_file:
            if data == ("find name,age from staff_table where age > %s" %(res[7])):
                line_age = line.split(',')[2]
                if int(line_age) > int(res[7]):
                    print(line)
            elif data == ('find * from staff_table where dept = %s'%(res[7])):
                line_dept = line.split(',')[4]
                temp_val = res[7].strip('"')
                if line_dept == temp_val:
                    print(line)
            elif data == ('find * from staff_table where enroll_date like %s'%(res[7])):
                line_enroll_date = line.split(',')[-1]
                temp_val2 = res[7].strip('"')
                if line_enroll_date.startswith(temp_val2):
                    print(line)



def add_employ(data):
    res = data.split(',')
    add_content_new = ' '.join(data.split(' ')[2:]).split(',')
    len_add_content = len(add_content_new)
    if data.startswith("add staff_table") and len_add_content == 5:
        add_content = ' '.join(data.split(' ')[2:])
        content_list = []
        staff_id = []

        phone_temp_list = []
        employ_file = open('employee_info','r+')
        for line in employ_file:
            person_phone = line.split(',')[3]
            id_num = int(line.split(',')[0])
            staff_id.append(id_num)
            phone_temp_list.append(person_phone)
            content_list.append(line.strip('\n'))
        if res[2] in phone_temp_list:
            print("手机号已存在")
        else:
            add_content = str(max(staff_id)+1)+','+add_content
            content_list.append(add_content)
            values = '\n'.join(content_list)
            employ_file.seek(0)
            employ_file.write(values)
            employ_file.truncate()
            employ_file.close()


            print("增加的内容为：",add_content)
    else:
        print("输入信息不对，重新输入")



def delete_employ(data):
    del_id = data.split('=')[1]
    if data.startswith("del from staff_table where"):
        content_list = []
        del_employ = open("employee_info",'r+')
        for line in del_employ:
            id_num = line.split(',')[0]
            if str(id_num) != del_id:
                content_list.append(line.strip('\n'))
            else:
                print("删除的员工信息：",line)
        values = '\n'.join(content_list)
        del_employ.seek(0)
        del_employ.write(values)
        del_employ.truncate()
        del_employ.close()

def modify_employ(data):
    temp_list = []
    update_info = []
    check_condition = data.split('=')[-1].strip()
    check_name = data.split()[7]
    update_value = data.split()[5]
    update_name = data.split()[3]
    employ_file_key = {0:'staff_id',1:'name',2:'age',3:'phone',4:'dept',5:'enroll_date'}
    for key,val in employ_file_key.items():
        if check_name == val:
            check_name_num = key
        if update_name == val:
            update_name_num = key
    modify_employ_table = open('employee_info', 'r+')
    for line in modify_employ_table:
        if line.split(',')[check_name_num] == check_condition:
            old_value = line.split(',')[update_name_num]
            res = line.replace(old_value,update_value)
            temp_list.append(res.strip('\n'))
            update_info.append(res)
        else:
            temp_list.append(line.strip('\n'))

    values = '\n'.join(temp_list)
    modify_employ_table.seek(0)
    modify_employ_table.write(values)
    modify_employ_table.truncate()
    modify_employ_table.close()
    for i in update_info:
        print(i)

if __name__ == "__main__":
    employ_dict = {
        "1":["查询",check_employ],
        "2":["添加",add_employ],
        "3":["删除",delete_employ],
        "4":["修改",modify_employ],
        "5":["退出",exit]
    }

    res = login()
    flag = True
    if res:
        while flag:
            choice = input("\033[34;1m1.查询，2.添加，3.删除，4.修改，5.退出:\033[0m").strip()
            if choice.isdigit() and int(choice) <len(employ_dict) and int(choice) > 0:
                while True:
                    operate_choice = input("\033[35;1m您将正在进行 %s 操作,帮助(H),返回(B),退出(Q)：\033[0m"% employ_dict[choice][0])
                    if len(operate_choice) == 0:continue
                    if operate_choice == 'H':
                        operate_statement(employ_dict[choice][0])
                    elif operate_choice == 'B':
                        break
                    elif operate_choice == 'Q':
                        flag = False
                        break
                    else:
                        employ_dict[choice][1](operate_choice)

            else:
                print("请输入正确的选项")

    else:
        print("exit")


'''
工厂函数
'''











