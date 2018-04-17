# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'yangyang'
__mtime__ = '2018.01.02'
"""

def login_auth(func):
    def inner(*args,**kwargs):
        global user_login_status
        name = 'ryan'
        old_password = '1111'
        login_name = input("login:").strip()
        password = input("password:").strip()
        if password == old_password and  login_name == name:
                func(login_name,*args,**kwargs)
    return inner


@login_auth
def run(username,age,address):
    print("login user is %s,age is %s,address is %s"%(username,age,address))

run(18,'SH')

