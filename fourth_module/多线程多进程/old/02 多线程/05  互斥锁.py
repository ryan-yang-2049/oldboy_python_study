# -*- coding: utf-8 -*-
"""
__title__ = '05  互斥锁.py'
__author__ = 'yangyang'
__mtime__ = '2018.01.31'
"""

# 互斥锁，保证数据安全，牺牲效率。
from threading import Thread,Lock
import time
n = 100

def task():
	global n
	mutex.acquire()
	temp = n
	time.sleep(0.1)
	n = temp - 1
	mutex.release()

if __name__ == '__main__':
	mutex = Lock()
	t_l = []
	for i in range(90):
		t = Thread(target=task)
		t_l.append(t)
		t.start()
	print(t_l)
	for t in t_l:       # 因主线程和子线程都是并发执行的，因此要先执行完子线程以后，主线程才能获取的子线程处理以后的值。
		t.join()

	print("主",n)











