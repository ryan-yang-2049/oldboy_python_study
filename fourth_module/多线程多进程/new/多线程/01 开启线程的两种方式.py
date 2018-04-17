# -*- coding: utf-8 -*-
"""
__title__ = '01 开启线程的两种方式.py'
__author__ = 'yangyang'
__mtime__ = '2018.02.07'
"""
from threading import Thread
import os,time
# def task(name):
# 	print("%s is running,PID: %s" % (name,os.getpid()))
#
# if __name__ == '__main__':
# 	p = Thread(target=task,args=('ryan',))
# 	p.start()
# 	print("主线程,PID:%s"%os.getpid())

class MyThread(Thread):
	def __init__(self,name):
		super().__init__()
		self.name = name

	def run(self):
		print("%s is running,PID: %s"%(self.name,os.getpid()))

if __name__ == '__main__':

	obj = MyThread('ryan')
	obj.start()
	print("主线程,PID: %s"%os.getpid())