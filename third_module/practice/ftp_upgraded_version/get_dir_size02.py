# -*- coding: utf-8 -*-
"""
__title__ = 'get_dir_size02.py'
__author__ = 'yangyang'
__mtime__ = '2018.01.19'
"""

import os

def calc_dir_size(path,res):
	for i in os.listdir(path):
		temp_dir = os.path.join(path,i)
		if os.path.isdir(temp_dir):
			calc_dir_size(temp_dir,res)
		else:
			res += os.path.getsize(temp_dir)
	return res


if __name__ == '__main__':
	dirname = r'D:\gitcode\oldboy_python_study\third_module\practice\ftp_upgraded_version\server\user_home\ryan'
	size = 0
	return_res = calc_dir_size(dirname,size)
	print(return_res)
