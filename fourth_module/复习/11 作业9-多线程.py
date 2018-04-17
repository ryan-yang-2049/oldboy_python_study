# -*- coding: utf-8 -*-
"""
__title__ = '11 作业9-多线程.py'
__author__ = 'yangyang'
__mtime__ = '2018.03.09'
"""


# from threading import Thread,currentThread
# import os,time
# def work():
# 	time.sleep(2)
# 	print('===>',currentThread().getName())
#
# if __name__ == '__main__':
# 	# start = time.time()
# 	# time.sleep(10)
# 	# stop = time.time()
# 	# print('run time is %s' % (stop - start))
#
# 	l=[]
# 	for i in range(5):
# 		p=Thread(target=work) #耗时2s多
# 		p.start()
# 		p.join()
# 	for i in range(5):
# 		p=Thread(target=work) #耗时2s多
# 		l.append(p)
# 		p.start()
# 	for p in l:
# 		p.join()

from threading import Thread
import os,time
import re,hashlib


info_dict = {}
def auth_info():
	count = 0
	while count<3:
		# count += 1
		username = input("username :").strip()
		if not  username:continue
		password = input("password:").strip()
		if not password:continue
		if len(password) <6 :continue
		obj = re.match('^[a-zA-Z](.*)$',password)
		if obj:
			info_dict[username]=password
			break

def save():
	pass



auth_info()
print(info_dict)



