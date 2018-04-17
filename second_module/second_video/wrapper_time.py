# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'yangyang'
__mtime__ = '2018.01.04'
"""
import time
"""
定义简单的装饰器,用来输出程序运行的所用时间
"""
def timer(func):
    def decor(*args):

        start_time = time.time()
        time.sleep(2)
        func(*args)
        end_time = time.time()
        run_time = end_time - start_time
        print("run the func use : ", run_time)
    return decor

@timer
def printSth(str, count):
    for i in range(count):
        print("%d hello,%s!"%(i,str))



printSth("world", 100)