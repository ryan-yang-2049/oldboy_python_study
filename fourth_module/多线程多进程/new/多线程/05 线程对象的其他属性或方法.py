# -*- coding: utf-8 -*-
"""
__title__ = '05 线程对象的其他属性或方法.py'
__author__ = 'ryan'
__mtime__ = '2018/2/7'
"""

'''
Thread实例对象的方法
  # isAlive(): 返回线程是否活动的。
  # getName(): 返回线程名。
  # setName(): 设置线程名。

threading模块提供的一些方法：
  # threading.currentThread(): 返回当前的线程变量。
  # threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
  # threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。
'''

from threading import  Thread,currentThread,enumerate,activeCount
import os

def task():
	print("%s is running,PID: %s" % (currentThread().getName(),os.getpid()))

if __name__ == '__main__':
	p = Thread(target=task)
	p.start()
	print(enumerate())
	print("主线程的名称：%s"%currentThread().getName())
	print("主线程",activeCount())
	print(enumerate())




