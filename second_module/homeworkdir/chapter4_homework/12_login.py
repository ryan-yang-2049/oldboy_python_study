#!/usr/bin/env python
#coding:utf-8

import io,json
import time
from datetime import datetime
import hashlib

def hash_val(arg):
    hash_value = hashlib.md5()
    hash_value.update(arg.encode(encoding='utf-8'))
    res = hash_value.hexdigest()
    return res

read_file = io.open('1234.json','r',encoding='utf-8')
info_dict = json.load(read_file)
print(info_dict)
read_file.close()

name = '1234'
count = 0
login_times_dict = {}
while count < 3:
    login_name = input("name:").strip()
    if info_dict['status'] == 1:
        print("用户被锁")
        break
    expire_date_info = time.mktime(time.strptime(info_dict["expire_date"],"%Y-%m-%d"))
    last_time = expire_date_info - time.time()
    if last_time < 0:
        print("已过期")
        break

    login_passwd = input("passwd:").strip()
    hash_passwd = hash_val(login_passwd)
    count += 1
    if login_name in login_times_dict:
        login_times_dict[login_name] += 1
    else:
        login_times_dict.setdefault(login_name,1)

    if login_name == name and hash_passwd == info_dict['password']:
        print("login success")
        info_dict['password']=hash_val(login_passwd)
        write_file = io.open('1234.json', 'w', encoding='utf-8')
        json.dump(info_dict, write_file)
        write_file.close()
        break

    else:
        print("login faild")
        if login_times_dict[login_name] == 3:
            print("输入错误信息超过三次")
            info_dict['status'] = 1
            write_file = io.open('1234.json','w',encoding='utf-8')
            json.dump(info_dict,write_file)
            write_file.close()
            break


