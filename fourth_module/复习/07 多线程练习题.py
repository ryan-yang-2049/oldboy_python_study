# -*- coding: utf-8 -*-
"""
__title__ = '07 多线程练习题.py'
__author__ = 'yangyang'
__mtime__ = '2018.03.08'
"""
from threading import Thread
import time

def foo():
    print(123)
    time.sleep(1)
    print("end123")

def bar():
    print(456)
    time.sleep(3)
    print("end456")

if __name__ == '__main__':
    t1=Thread(target=foo)
    t2=Thread(target=bar)

    t1.daemon=True
    t1.start()
    t2.start()
    print("main-------")









