# -*- coding: utf-8 -*-
"""
__title__ = '07 模拟抢票.py'
__author__ = 'yangyang'
__mtime__ = '2018.01.29'
"""

from  multiprocessing import  Process,Lock
import time,json

def search(name):
	'''
	查看剩余票的余额
	'''
	time.sleep(1)
	dic = json.load(open('db.txt','r',encoding='utf-8'))
	print('<%s> 查看到的剩余票数位: 【%s】'%(name,dic['count']))

def get(name):
	'''
	开始进行抢票操作
	'''
	time.sleep(1)
	dic = json.load(open('db.txt','r',encoding='utf-8'))

	if dic['count'] >0:
		dic['count'] -= 1
		time.sleep(1)
		json.dump(dic,open('db.txt','w',encoding='utf-8'))
		print('<%s> 购票成功' %name)
	else:
		print('<%s> 购票失败' % name)

def task(name,mutex):
	search(name)
	mutex.acquire()
	get(name)
	mutex.release()

if __name__ == '__main__':
	mutex = Lock()
	for i  in range(5):
		p=Process(target=task,args=('路人 %s'%i,mutex))
		p.start()











