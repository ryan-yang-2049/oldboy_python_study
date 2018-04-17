# -*- coding: utf-8 -*-
"""
__title__ = 'settings.py'
__author__ = 'yangyang'
__mtime__ = '2018.01.16'
"""

import os
import hashlib
import configparser

if os.name == 'posix':	#linux or mac
	# user_home_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/user_home'
	user_config = os.path.dirname(os.path.abspath(__file__))+'/userinfo.ini'
	PATH_SYMBOL = '/'
	coding = 'utf-8'
# windows
elif os.name == 'nt':
	# user_home_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'\\user_home'
	user_config = os.path.dirname(os.path.abspath(__file__))+'\\userinfo.ini'
	PATH_SYMBOL = '%s' % ('\\')
	coding = 'gbk'





def getfilemd5(filename):
	'''
	文件的md5校验规则： 文件名+文件内容进行校验
	:param filename:
	:return:
	'''
	filemd5 = None
	if os.path.isfile(filename):
		f = open(filename,'rb')
		md5_obj = hashlib.md5()
		data = f.read()
		content = ("%s%s"%(filename,data)).encode('utf-8')
		md5_obj.update(content)
		hash_code = md5_obj.hexdigest()
		f.close()
		filemd5 = str(hash_code).lower()
	return filemd5

def file_info(filename):
	'''
	获取文件信息字典
	:param filename:
	:return:
	'''
	file_info_dict = {}
	if os.path.exists(filename) and os.path.isfile(filename):
		file_info_dict['file_md5'] = getfilemd5(filename)
		file_info_dict['file_size'] = os.path.getsize(filename)
		file_info_dict['file_name'] = filename
	return file_info_dict


def calc_dir_size(path,res):
	'''
	计算某个目录的大小：包含子目录的文件全部大小。
	path:路径参数，
	res：返回结果
	'''
	for i in os.listdir(path):
		temp_dir = os.path.join(path, i)
		if os.path.isdir(temp_dir):
			calc_dir_size(temp_dir,res)
		else:
			res += os.path.getsize(temp_dir)
	return res

def user_home(username):
	if os.name == 'posix':
		userhome = "%s%s%s%s%s"%(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),PATH_SYMBOL,'user_home',PATH_SYMBOL,username)
		return userhome
	if os.name == 'nt':
		userhome = "%s%s%s%s%s"%(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),PATH_SYMBOL,'user_home',PATH_SYMBOL,username)
		return userhome

class UserManage(object):
	def __init__(self,name,passwd):
		self.name = name
		self.passwd = self.md5_encryption(passwd)
		# self.user_home_dir = "%s/%s"%(user_home_dir,self.name)
		self.user_home = user_home(self.name)
		self.conf = configparser.ConfigParser()

	@staticmethod
	def md5_encryption(arg):
		'''
		密码生成md5值
		:param arg:
		:return:
		'''
		hash_obj = hashlib.md5()
		hash_obj.update(arg.encode(encoding=coding))
		hash_res = hash_obj.hexdigest()
		return hash_res

	def create_user(self):
		'''
		1.先添加到配置文件
		1.1 configure 必须先读才能去写，不然会覆盖
		2.创建对应的家目录
		:return:
		'''

		self.conf.read(user_config)
		section_li = self.conf.sections()
		if self.name in section_li:
			print("用户已存在")
			return
		self.conf.add_section(self.name)
		self.conf[self.name]['password'] = self.passwd
		self.conf[self.name]['home_dir'] = self.user_home
		self.conf[self.name]['disk_quota_kb'] = '100'
		self.conf.write(open(user_config,'w'))
		# 创建对应的家目录
		if not os.path.exists(self.user_home):
			os.mkdir(self.user_home)

	def auth_user(self):
		'''
		用于用户登录的时候的用户认证方法
		:return:
		'''
		# conf = configparser.ConfigParser()
		self.conf.read(user_config)
		if self.conf.has_section(self.name) and self.passwd == self.conf.get(self.name,'password'):
			print('login success')
			return True
		else:
			print("faild")
			return False

	def check_user_quota(self):
		'''
		用于查看用户配额的方法

		'''
		# conf = configparser.ConfigParser()
		self.conf.read(user_config)
		read_info = self.conf.items(self.name)
		return read_info[2][1]





if __name__ == '__main__':
	while True:
		print("------管理页面------")
		username = input("创建的用户名,退出(Q)：").strip()
		if username == 'Q':break
		password = input("密码：").strip()
		obj = UserManage(username, password)
		obj.create_user()

# obj = UserManage('ryan','1234')
# user_disk_quota = obj.check_user_quota()
# print(user_disk_quota)

# print(user_home('ryan'))