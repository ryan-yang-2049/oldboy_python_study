# -*- coding: utf-8 -*-
"""
__title__ = 'client_startup.py'
__author__ = 'yangyang'
__mtime__ = '2018.02.02'
"""
import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)
# print(sys.path)
# print(BASE_DIR)

from client.core import ftpclient




'''
登录名    密码
ryan     1234
cherry   1234
alex     1234
'''

if __name__ == '__main__':
	IP = '127.0.0.1'
	Port = 8904
	client=ftpclient.FtpClient((IP,Port))
	client.login()




