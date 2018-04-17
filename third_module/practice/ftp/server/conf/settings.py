# -*- coding: utf-8 -*-
"""
__title__ = 'settings.py'
__author__ = 'yangyang'
__mtime__ = '2018.01.16'
"""

import os,sys
import hashlib
import configparser

if os.name == 'posix':	#linux or mac
    user_home_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/user_home'
    user_config = os.path.dirname(os.path.abspath(__file__))+'/userinfo.ini'
# windows
elif os.name == 'nt':
	user_home_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'\\user_home'
	user_config = os.path.dirname(os.path.abspath(__file__))+'\\userinfo.ini'

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




class UserManage(object):
	def __init__(self,name,passwd):
		self.name = name
		self.passwd = self.md5_encryption(passwd)
		self.user_home_dir = "%s/%s"%(user_home_dir,self.name)

	@staticmethod
	def md5_encryption(arg):
		'''
		密码生成md5值
		:param arg:
		:return:
		'''
		hash_obj = hashlib.md5()
		hash_obj.update(arg.encode(encoding='utf-8'))
		hash_res = hash_obj.hexdigest()
		return hash_res

	def create_user(self):
		'''
		1.先添加到配置文件
		1.1 configure 必须先读才能去写，不然会覆盖
		2.创建对应的家目录
		:return:
		'''
		conf = configparser.ConfigParser()
		conf.read(user_config)
		conf.add_section(self.name)
		conf[self.name]['password'] = self.passwd
		conf[self.name]['home_dir'] = self.user_home_dir
		conf[self.name]['disk_quota_kb'] = '100'
		conf.write(open(user_config,'w'))
		# 创建对应的家目录
		if not os.path.exists(self.user_home_dir):
			os.mkdir(self.user_home_dir)

	def auth_user(self):
		'''
		用于用户登录的时候的用户认证方法
		:return:
		'''
		conf = configparser.ConfigParser()
		conf.read(user_config)
		if conf.has_section(self.name) and self.passwd == conf.get(self.name,'password'):
			print('login success')
			return True
		else:
			print("faild")
			return False

	def check_user_info(self):
		'''
		用于查看用户配额的方法
		:return:
		'''
		conf = configparser.ConfigParser()
		conf.read(user_config)
		read_info = conf.items(self.name)
		print("用户家目录：%s"%read_info[1][1])
		print("磁盘配额大小：%s"%read_info[2][1])



if __name__ == '__main__':
	while True:
		print("管理页面，创建用户信息")
		username = input("创建的用户名,退出(Q)：").strip()
		if username == 'Q':break
		password = input("密码：").strip()
		obj = UserManage(username, password)
		obj.create_user()