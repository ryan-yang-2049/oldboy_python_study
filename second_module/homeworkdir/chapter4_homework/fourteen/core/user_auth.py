#coding:utf-8

import os,sys
import hashlib
import time
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from bin import start

def hash_val(arg):
    hash_obj = hashlib.md5()
    hash_obj.update(arg.encode(encoding='utf-8'))
    hash_res = hash_obj.hexdigest()
    return hash_res


user_login_status = False

def login(func):
    def inner(*args,**kwargs):
        global user_login_status
        login_times_dict = {}
        count = 0
        while count < 3:
            login_name = input("login:").strip()
            count += 1
            if login_name in login_times_dict:
                login_times_dict[login_name] += 1
            else:
                login_times_dict.setdefault(login_name,1)
            user_info_dict = start.operate_json_file(login_name,'read')
            expire_date_file = time.mktime(time.strptime(user_info_dict["expire_date"],"%Y-%m-%d"))
            last_time = expire_date_file - time.time()
            if last_time < 0:
                print("用户已过期")
                break

            if user_info_dict['status'] == 1:
                print("用户被锁，请联系管理员：11066986@qq.com")
                '''
                可以加发送邮件
                '''
                break
            password = input("password:").strip()
            hash_password = hash_val(password)
            if hash_password == user_info_dict['password']:
                print("欢迎来到本系统")
                user_login_status = True

                if user_login_status == True:
                    func(*args,**kwargs)
            else:
                print("密码错误！")
                if login_times_dict[login_name] == 3:
                    print(login_times_dict)
                    user_info_dict['status'] = 1
                    start.operate_json_file(login_name,'write',data=user_info_dict)


    return inner


@login
def auth():
    print("aaa")


auth()






