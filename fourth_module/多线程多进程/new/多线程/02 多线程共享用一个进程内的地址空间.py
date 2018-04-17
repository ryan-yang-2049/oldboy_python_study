# -*- coding: utf-8 -*-
"""
__title__ = '02 多线程共享用一个进程内的地址空间.py'
__author__ = 'yangyang'
__mtime__ = '2018.02.07'
"""

from threading import  Thread
import os,time

n = 100
def task():
	global n
	n -= 10

if __name__ == '__main__':
	t = Thread(target=task)
	t.start()
	print("主进程 n=%s"%n) # 主进程 n=0







