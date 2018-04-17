# -*- coding: utf-8 -*-
"""
__title__ = '15 map功能补充.py'
__author__ = 'yangyang'
__mtime__ = '2018.02.05'
"""

from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
import os,time,random


def task(n):
    print('%s is running' %os.getpid())
    time.sleep(2)
    return n**2


if __name__ == '__main__':
    p=ProcessPoolExecutor()
    obj=p.map(task,range(10))       # 返回的是一个可迭代对象
    p.shutdown()
    print('='*30)
    print(list(obj))


'''
1.进程池线程池
2.回调函数
3.queue  实现分布式编程
3.1 生产者消费者模型。


'''







