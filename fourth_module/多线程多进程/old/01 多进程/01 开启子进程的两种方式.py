# -*- coding: utf-8 -*-
"""
__title__ = '01 开启子进程的两种方式.py'
__author__ = 'yangyang'
__mtime__ = '2018.01.29'
"""

#方式一：
from multiprocessing import  Process
import time
def task(name):
	print('%s is running'%name)
	time.sleep(3)
	print('%s is done'%name)



if __name__ == '__main__':
	p=Process(target=task,args=('子进程1',))
	# Process(target=task,kwargs={'name':'子进程2'})
	p.start()   # 仅仅只是给操作系统发送了一个信号。
	print('主')

# 方式二:

from multiprocessing import  Process
import  time
class MyProcess(Process):

	def __init__(self,name):
		super().__init__()
		self.name = name

	def run(self):
		print('%s is running'%self.name)
		time.sleep(1)
		print('%s is done'%self.name)


if __name__ == '__main__':
	p=MyProcess('子进程1')
	p.start()











