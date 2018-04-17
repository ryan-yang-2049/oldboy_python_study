# -*- coding: utf-8 -*-
"""
__title__ = '08 信号量.py'
__author__ = 'yangyang'
__mtime__ = '2018.02.01'
"""

from threading import Thread,Semaphore,currentThread
import  time,random

sm=Semaphore(2)
# n=10
def task():
	# sm.acquire()
	# print("%s running"%currentThread().getName())
	# time.sleep(random.randint(1, 3))
	# sm.release()
	#等价于下面
	# global n
	with sm:
		print("%s running" % currentThread().getName())
		# n -= 10
		print("inner",n)
		time.sleep(2)

if __name__ == '__main__':
	t_l = []
	for i in range(3):
		t=Thread(target=task)
		t.start()
		t_l.append(t)

	for t in t_l:
		t.join()
	# print('n',n)








