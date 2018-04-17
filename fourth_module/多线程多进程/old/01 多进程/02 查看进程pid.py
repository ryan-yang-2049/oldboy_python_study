# -*- coding: utf-8 -*-
"""
__title__ = '02 查看进程pid.py'
__author__ = 'yangyang'
__mtime__ = '2018.01.29'
"""

from multiprocessing import  Process
import time,os
def task(name):
	print('%s is running，pid is %s'%(name,os.getpid()))
	time.sleep(3)
	print('%s is done,parent pid is ==> %s'%(name,os.getppid()))



if __name__ == '__main__':
	p=Process(target=task,args=('子进程1',))
	# Process(target=task,kwargs={'name':'子进程2'})
	p.start()   # 仅仅只是给操作系统发送了一个信号。
	print('主',os.getpid(),os.getppid())  # 这个是主进程，当然 运行print 的主主进程是pycharm或者终端 ,windows 查看进程 tasklist |findstr pycharm














