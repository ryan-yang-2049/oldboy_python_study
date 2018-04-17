# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'yangyang'
__mtime__ = '2018.01.16'
"""



import socket
import subprocess
import struct
import json
import os,sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from server.conf import settings

phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
phone.bind(('127.0.0.1',8081)) #0-65535:0-1024给操作系统使用
phone.listen(5)


while True: # 链接循环
	print('starting...')
	conn,client_addr=phone.accept()
	while True:
		res = conn.recv(1024)
		if not res:continue
		user_dict = json.loads(res.decode('utf-8'))	# dict
		user_name = user_dict['username']
		password = user_dict['password']
		login_auth = settings.UserManage(user_name,password)

		res = login_auth.auth_user()
		print('11111',res,type(res))
		res_bytes = (json.dumps(res)).encode('utf-8')
		conn.send(res_bytes)
		if res:
			print("success")
	else:
		print("faild1")
		break
	conn.close()


phone.close()








