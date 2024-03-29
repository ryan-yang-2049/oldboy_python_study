# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'yangyang'
__mtime__ = '2018.01.17'
"""

import os,sys
import hashlib

if os.name == 'posix':
	PATH_SYMBOL = '/'
if os.name == 'nt':
	PATH_SYMBOL = '%s' % ('\\')


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

	file_info_dict = {}
	if os.path.exists(filename) and os.path.isfile(filename):
		file_info_dict['file_md5'] = getfilemd5(filename)
		file_info_dict['file_size'] = os.path.getsize(filename)
		file_info_dict['file_name'] = filename
		return file_info_dict
	# else:
	# 	return False

def user_home(username):
	if os.name == 'posix':
		userhome = "%s%s%s%s%s"%(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),PATH_SYMBOL,'client_user_home',PATH_SYMBOL,username)
		return userhome
	if os.name == 'nt':
		userhome = "%s%s%s%s%s"%(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),PATH_SYMBOL,'client_user_home',PATH_SYMBOL,username)
		return userhome


# userhome_format = D:\gitcode\oldboy_python_study\fourth_module\homework\ftp_thread\client\client_user_home\ryan

# res = file_info(r"D:\gitcode\oldboy_python_study\fourth_module\homework\ftp_thread\client\client_user_home\ryan\3.jpeg")
# print(res)