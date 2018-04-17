# -*- coding: utf-8 -*-
"""
__title__ = '08 互斥锁与join的区别.py'
__author__ = 'yangyang'
__mtime__ = '2018.01.29'
"""

from  multiprocessing import  Process,Lock
import time,json

def search(name):
	time.sleep(1)
	dic = json.load(open('db.txt','r',encoding='utf-8'))
	print('<%s> 查看到的剩余票数位: 【%s】'%(name,dic['count']))

def get(name):

	time.sleep(1)
	dic = json.load(open('db.txt','r',encoding='utf-8'))

	if dic['count'] >0:
		dic['count'] -= 1
		time.sleep(1)
		json.dump(dic,open('db.txt','w',encoding='utf-8'))
		print('<%s> 购票成功' %name)
	else:
		print('<%s> 购票失败' % name)

def task(name):
	search(name)
	get(name)

if __name__ == '__main__':
	for i  in range(10):
		p=Process(target=task,args=('路人 %s'%i,))
		p.start()
		p.join()










