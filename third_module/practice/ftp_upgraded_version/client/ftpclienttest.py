# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'yangyang'
__mtime__ = '2018.01.16'
"""


import socket
import struct
import json,os,sys
import hashlib

def client_login():
	user_dict = {}
	while True:
		user_dict['username'] = input("login:").strip()
		if len(user_dict['username']) == 0: continue
		user_dict['password'] = input("password:").strip()
		if len(user_dict['password']) == 0: continue
		user_dict_bytes = (json.dumps(user_dict)).encode('utf-8')

		phone.send(user_dict_bytes)
		# res = json.loads(phone.recv(1024))
		res_obj = phone.recv(1024)
		print(res_obj, type(res_obj))
		res = json.loads(res_obj)

		if res:
			print('success')
			'''验证成功 开始执行上传下载等'''
			pass



phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.connect(('127.0.0.1',8080))
client_login()


phone.close()



import  os,sys
file_info1 = {
	'file_name':'a.txt',
	'file_md5':'12121212',
	'file_size':'os.path.getsize(filename)'

}

def getfilemd5(filename):
	filemd5 = None
	if os.path.isfile(filename):
		f = open(filename,'rb')
		md5_obj = hashlib.md5()
		while True:
			data = f.read(102400)
			if not data:break
			md5_obj.update(data)
		hash_code = md5_obj.hexdigest()
		f.close()
		filemd5 = str(hash_code).lower()
	return filemd5


def file_info(filename):
	file_info_dict = {}
	if os.path.exists(filename) and os.path.isfile(filename):
		file_info_dict['file_md5'] = getfilemd5(filename)
		file_info_dict['file_size'] = os.path.getsize(filename)
		file_info_dict['file_name'] = filename
		return file_info_dict
	else:
		return False








