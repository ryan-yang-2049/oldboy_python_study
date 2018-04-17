# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'yangyang'
__mtime__ = '2018.01.17'
"""

import os,sys
import hashlib

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
	else:
		return False
