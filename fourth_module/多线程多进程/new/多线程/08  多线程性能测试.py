# -*- coding: utf-8 -*-
"""
__title__ = '08  多线程性能测试.py'
__author__ = 'yangyang'
__mtime__ = '2018.02.08'
"""
# 如果并发的多个任务是计算密集型：多进程效率高
from multiprocessing import Process
from threading import Thread
import os,time
def work():
    res=0
    for i in range(100000000):
        res*=i


if __name__ == '__main__':
    l=[]
    print(os.cpu_count()) #本机为4核
    start=time.time()
    for i in range(4):
        # p=Process(target=work) #耗时21s多
        p=Thread(target=work) #耗时62多
        l.append(p)
        p.start()
    for p in l:
        p.join()
    stop=time.time()
    print('run time is %s' %(stop-start))


#如果并发的多个任务是I/O密集型：多线程效率高
from multiprocessing import Process
from threading import Thread
import threading
import os,time
def work():
    time.sleep(2)
    print('===>')

if __name__ == '__main__':
    l=[]
    print(os.cpu_count()) #本机为4核
    start=time.time()
    for i in range(400):
        p=Process(target=work) #耗时52s多,大部分时间耗费在创建进程上
        # p=Thread(target=work) #耗时2s多
        l.append(p)
        p.start()
    for p in l:
        p.join()
    stop=time.time()
    print('run time is %s' %(stop-start))










