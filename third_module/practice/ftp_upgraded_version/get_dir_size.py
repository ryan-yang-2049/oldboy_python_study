# -*- coding: utf-8 -*-
"""
__title__ = 'get_dir_size.py'
__author__ = 'yangyang'
__mtime__ = '2018.01.19'
"""


import os,json

def list_dir(path,res,res_li):
	for i in os.listdir(path):
		temp_dir = os.path.join(path, i)
		if os.path.isdir(temp_dir):
			temp =  []
			res.append(list_dir(temp_dir, temp,res_li))
		else:
			res_li.append(temp_dir)
	return res_li


if __name__ == '__main__':
	dirname = r'D:\gitcode\oldboy_python_study\third_module\practice\ftp_upgraded_version\server\user_home\ryan'
	res_li = []
	res  =  []
	return_res = list_dir(dirname,res,res_li)
	print(return_res)
	total_size = 0
	for i in return_res:
		print(i,"size:",os.path.getsize(i))
		total_size += os.path.getsize(i)
	print(total_size)
