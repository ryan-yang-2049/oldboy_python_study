# -*- coding: utf-8 -*-
"""
__title__ = '03 Thread对象的其他属性和方法.py'
__author__ = 'yangyang'
__mtime__ = '2018.01.31'
"""

from threading import Thread,currentThread,active_count,enumerate
import time


def task():
	print('%s is running'%currentThread().getName())
	time.sleep(2)
	print('%s is running'%currentThread().getName())


if __name__ == '__main__':
	t1 = Thread(target=task,name="Thread-test-1")
	t1.start()
	t2 = Thread(target=task,name="Thread-test-2")
	t2.start()
	t1.setName('子线程1')  # 设置子线程名称
	print("查看存活的线程总数", active_count())	       # 查看存活的线程总数
	t1.join()           # 让子线程先执行完毕后在执行后面的
	currentThread().setName('Main Thread name')     # 设置主线程名称
	# 查看线程是否存活
	print(t1.isAlive())
	print("主线程",currentThread().getName())   # 主线程名称：MainThread
	# enumerate 以列表形式获取当前活跃的线程对象。[<_MainThread(MainThread, started 78460)>, <Thread(Thread-test-1, started 76708)>]
	print(enumerate())




