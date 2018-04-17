# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'yangyang'
__mtime__ = '2018.01.16'
"""




import hashlib
import os

# def getfilemd5(filename):
# 	filemd5 = None
# 	if os.path.isfile(filename):
# 		f = open(filename,'rb')
# 		md5_obj = hashlib.md5()
# 		md5_obj.update(f.read())
# 		hash_code = md5_obj.hexdigest()
# 		f.close()
# 		filemd5 = str(hash_code).lower()
# 	return filemd5
#
# res = getfilemd5('ex01.py')			#如果是带斜线的 要+ r 去让他是原来意思
# print(res)
#
#
# # 919d1ce06395084bb5007828173adca7
# # 3833e947ddcbeb9fe898843f1bb3538c
# # 3833e947ddcbeb9fe898843f1bb3538c


# def getfilemd5(filename):
# 	filemd5 = None
# 	if os.path.isfile(filename):
# 		f = open(filename,'rb')
# 		md5_obj = hashlib.md5()
# 		while True:
# 			data = f.read(100000)
# 			if not data:break
# 			md5_obj.update(data)
# 		hash_code = md5_obj.hexdigest()
# 		f.close()
# 		filemd5 = str(hash_code).lower()
# 	return filemd5
#
#
#
# res = getfilemd5(user_config)			#如果是带斜线的 要+ r 去让他是原来意思
# print(res)





