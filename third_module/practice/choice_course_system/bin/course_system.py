# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'yangyang'
__mtime__ = '2018.01.10'
"""
import os,sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


from conf.create_role_info import UserRoleInfo
# from core.main import Login
from core.main import ManageView
from core.main import StudentView
from core.main import TeacherView

'''
程序入口文件：
 角色       登录名       密码
admin      admin        1234
teacher    alex         1234
teacher    egon         1234
student    ryan1        1234
student    ryan2        1234
.....
student    cherry1      1234
student    cherry2      1234
.....

'''

if __name__ == '__main__':
    print("\033[34;0m welcome to course system \033[0m")
    while True:
        choice_info = {'1':['管理登陆',ManageView],
                       '2':['教师登陆',TeacherView],
                       '3':['学生登陆',StudentView],
                       '4':['注册',UserRoleInfo.create_user],
                       '5':['退出',sys.exit]}

        for key,val in choice_info.items():
            print("\033[31;0m %s:%s\033[0m"%(key.center(3),str(val[0]).center(8)))
        choice = input("请选择：").strip()
        if choice not in choice_info:continue
        choice_info[choice][1]()

