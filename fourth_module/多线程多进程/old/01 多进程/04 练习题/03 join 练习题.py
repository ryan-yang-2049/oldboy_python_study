# -*- coding: utf-8 -*-
"""
__title__ = '03 join 04 练习题.py'
__author__ = 'yangyang'
__mtime__ = '2018.01.29'
"""

from multiprocessing import Process
import time
import random

def task(n):
    time.sleep(random.randint(1,3))
    print('-------->%s' %n)

if __name__ == '__main__':
    p1=Process(target=task,args=(1,))
    p2=Process(target=task,args=(2,))
    p3=Process(target=task,args=(3,))

    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()

    print('-------->4')










