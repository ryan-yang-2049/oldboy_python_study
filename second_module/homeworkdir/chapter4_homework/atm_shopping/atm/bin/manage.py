#coding:utf-8

import os,sys
import hashlib

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR)
# print(BASE_DIR)
from core.log_info import log_output
from core.file_operate import operate_user_info_file


#生成hash_md5值
def hash_val(arg):
    hash_obj = hashlib.md5()
    hash_obj.update(arg.encode(encoding='utf-8'))
    hash_res = hash_obj.hexdigest()
    return hash_res

#用户注册
def user_registration():
    while True:
        regist_user = input("注册用户名:").strip()
        verification_user = operate_user_info_file(regist_user,'read')
        if not verification_user:
            regist_password = input("密码:").strip()
            passwd_hash_value = hash_val(regist_password)

            user_info_dict = {
                'username': regist_user,
                'password': passwd_hash_value,
                'status': 0,
                'expire_date': '2020-01-01',
                'quota': 15000.0,
                'balance': 15000.0,
            }
            operate_user_info_file(regist_user,'write',data=user_info_dict)
            message = "create user,the user is %s"%(regist_user)
            log_output('administrator', 'manage', "INFO", message=message)
            return True
        else:
            print("用户名已存在")
            continue
#修改密码
def modify_password():
    count = 0
    while count < 3:
        name = input("请输入需要修改密码的用户,退出（B）:").strip()
        if name == 'B':break
        judge_user = operate_user_info_file(name,'read')
        if judge_user:
            old_password = input("旧密码：")
            count += 1
            old_password_value = hash_val(old_password)
            user_info_dict = operate_user_info_file(name,'read')
            if old_password_value == user_info_dict['password']:
                new_password = input("新密码:").strip()
                new_password = hash_val(new_password)
                user_info_dict['password'] = new_password
                operate_user_info_file(name,'write',data=user_info_dict)
                message = "modify %s  password"%(name)
                log_output('administrator', 'manage', "INFO", message=message)

                return
            else:
                print("密码错误,请重新输入。")
        else:
            print("用户不存在")


def  modify_user_quota():
    flag = True
    while flag:
        username = input("请输入提升额度的账户,返回（B）:").strip()
        if username == 'B':break
        judge_user = operate_user_info_file(username,'read')
        if judge_user:
            while True:
                user_quota = judge_user['quota']
                add_user_quota = input("提升用户额度（RMB）,退出(Q)").strip()
                if add_user_quota == 'Q':
                    flag = False
                    break
                if not add_user_quota.isdigit():continue
                now_user_quota = user_quota + int(add_user_quota)
                judge_user['quota'] = now_user_quota
                operate_user_info_file(username,'write',data=judge_user)
                message = "increase user quota,%s old quota is %s,now quota is %s" % (username,user_quota,now_user_quota)
                log_output('administrator', 'manage', "INFO", message=message)
                break


def modify_user_status():
    operate_info_dict = {'F':['冻结','freeze',1],
                         'A':['激活','activation',0]
                         }
    flag =  True
    while flag:
        choice = input("冻结用户(F),激活账户(A),退出(B):").strip()
        if choice == 'B':
            break
        if choice == 'F' or choice =='A':
            while True:
                username = input("%s的账户名为,返回（B）："%(operate_info_dict[choice][0])).strip()
                if username == 'B':
                    flag = False
                    break
                judge_user = operate_user_info_file(username, 'read')
                if judge_user:
                    user_info_dict = operate_user_info_file(username,'read')
                    user_info_dict['status'] = operate_info_dict[choice][2]
                    operate_user_info_file(user_info_dict,'write',data=user_info_dict)
                    message = "%s user is %s " % (operate_info_dict[choice][1],username)
                    print(message)
                    log_output('administrator', 'manage', "INFO", message=message)
                    break
                else:
                    print("用户不存在,请重新输入")






#管理界面
if __name__ == '__main__':
    while True:
        manage_operate_dict = {'1':['用户注册',user_registration],
                               '2':['修改用户密码',modify_password],
                               '3':['修改用户额度',modify_user_quota],
                               '4':['修改用户状态',modify_user_status],
                               '5':['退出',sys.exit],

                               }
        for key,val in manage_operate_dict.items():
            print(key,val[0])
        choice = input("请选择序号进行操作：").strip()
        if choice in manage_operate_dict:
            manage_operate_dict[choice][1]()





