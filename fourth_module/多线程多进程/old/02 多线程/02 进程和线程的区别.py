# -*- coding: utf-8 -*-
"""
__title__ = '02 进程和线程的区别.py'
__author__ = 'yangyang'
__mtime__ = '2018.01.31'
"""

#1、开进程的开销远大于开线程
# import time
# from threading import  Thread
# from multiprocessing import Process
#
# def piao(name):
# 	print('%s piaoing' %name)
# 	time.sleep(2)
# 	print('%s piao end'%name)
#
# if __name__ == '__main__':
# 	t1_start = time.time()
# 	t1 = Thread(target=piao,args=('egon',))
# 	t1.start()
# 	print("开启线程一共运行了：",time.time()-t1_start) #0.0005
# 	p1_start = time.time()
# 	p1 = Process(target=piao,args=('egon',))
# 	p1.start()
# 	print("开启进程一共运行了：", time.time() - p1_start) #0.033
# 	print("主")

#2、同一进程内的多个线程共享该进程的地址空间
# import time
# from threading import  Thread
# from multiprocessing import Process
#
# n=100
# def task():
# 	global n
# 	n=0
#
# if __name__ == '__main__':
# 	t1 = Thread(target=task())
# 	t1.start()
#
# 	p1 = Process(target=task)
# 	p1.start()
# 	p1.join()
#
# 	print("主",n)

#3、所有子线程与主线程（主进程）是同一个PID号，子进程的PPID是主进程的PID
import time,os
from threading import  Thread
from multiprocessing import Process

def task(name):
	print("%s PID号: %s,PPID号：%s"%(name,os.getpid(),os.getppid()))

if __name__ == '__main__':
	p1 = Process(target=task,args=('子进程',))
	p1.start()
	p1.join()
	t1 = Thread(target=task,args=('子线程1',))
	t1.start()
	t2 = Thread(target=task,args=('子线程2',))
	t2.start()
	print("主进程 PID号: %s,PPID号：%s"%(os.getpid(),os.getppid()))

'''
子进程 PID号: 68240,PPID号：73452
子线程1 PID号: 73452,PPID号：13160
子线程2 PID号: 73452,PPID号：13160
主进程 PID号: 73452,PPID号：13160
'''







