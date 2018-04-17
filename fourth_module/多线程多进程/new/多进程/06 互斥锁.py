# -*- coding: utf-8 -*-
"""
__title__ = '06 互斥锁.py'
__author__ = 'ryan'
__mtime__ = '2018/2/6'
"""
# 互斥锁，保证数据安全，牺牲效率
from multiprocessing import  Process,Lock
import os,time

def work(mutex):
	mutex.acquire()
	print("task[%s] is running"%os.getpid())
	time.sleep(1)
	print("task[%s] is done"%os.getpid())
	mutex.release()

if __name__ == '__main__':
	mutex = Lock()
	p1 = Process(target=work,args=(mutex,))
	p2 = Process(target=work,args=(mutex,))
	p3 = Process(target=work,args=(mutex,))
	p1.start()   # 发通知给操作系统开进程
	p2.start()   # 发通知给操作系统开进程
	p3.start()   # 发通知给操作系统开进程
	print("主进程")
































