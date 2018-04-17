#!/usr/bin/env python
#coding:utf-8
'''
用户输入账户密码进行登陆
用户信息保存在文件内
用户密码输入错误三次后锁定用户，下次再登陆，检测到是这个用户也登录不了
'''

def login_auth(username,password):
    temp_list = []
    f = open("userinfo.txt",'r+')
    for line in f:
        if username in line:
            old_times = line.split(':')[2]
            print(old_times)
            if old_times > 3:
                return "username was being lock！"
            old_password = line.split(':')[1]
            if password != old_password:
                return "password is wrong！"






#
# count = 0
# login_info_dic = {}
# while True:
#     username = input("login:").strip()
#     password = input("passwd:").strip()

login_auth('cherry','b','c')




