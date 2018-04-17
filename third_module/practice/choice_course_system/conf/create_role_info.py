# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'yangyang'
__mtime__ = '2018.01.10'
"""
import pickle,os,sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core import file_manage

class UserRoleInfo(object):
    '''在用户注册时写入和读取用户的信息'''
    __verification_code = '10086'
    __user_data = file_manage.user_data
    __login_status = 0

    def __init__(self,name,passwd,role):
        self.name = name
        self.passwd = passwd
        self.role = role

    def verification_user(self):
        if self.role not in self.__user_data:
            return False
        if self.name not in self.__user_data[self.role]:
            return False
        if self.passwd != self.__user_data[self.role][self.name]['passwd']:
            return False

        user_info_dict = self.__user_data[self.role][self.name]
        return user_info_dict

    @classmethod
    def create_user(cls):
        '''
        创建用户
        用户字典信息：admin':{'role':'admin','passwd':'1234','login_statsu':0}
        '''

        while True:
            name = input("username:").strip()
            if len(name) == 0:continue
            passwd = input("password:").strip()
            role = input("role:").strip()
            if role not in cls.__user_data:
                print("请输入正确的角色名称：管理员：admin，教师：teacher,学生：teacher")
                continue
            if role == 'admin' or role == 'teacher':
                verification_code = input("创建 %s 需要验证码！"%(role)).strip()
                if verification_code != cls.__verification_code:
                    print("验证码错误,请重新输入信息！")
                    continue

            if name in cls.__user_data[role]:
                print("用户已存在！")
                continue
            cls.__user_data[role].update({name:{'role':role,'passwd':passwd,'login_status':cls.__login_status}})
            file_manage.file_operate('userinfo', 'w', data=cls.__user_data)
            break

# UserRoleInfo.create_user()















