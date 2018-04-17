# -*- coding: utf-8 -*-
"""
__title__ = '08  守护进程.py'
__author__ = 'ryan'
__mtime__ = '2018/2/6'
"""


from multiprocessing import Process
import os,time

def work():
	print("%s is working"%os.getpid())
	time.sleep(3)
	print("%s is done"%os.getpid())

if __name__ == '__main__':
	# 第一种情况，当一起join的时候，程序运行的时间就是最长的那个进程运行时间
	# p1 = Process(target=work)
	# p2 = Process(target=work)
	# p3 = Process(target=work)
	# p1.start()
	# p2.start()
	# p3.start()
	# p1.join()
	# p2.join()
	# p3.join()

	# 第二种情况，当分开join的时候，那么这个开启子进程的方式就相当于是串行了。
	p1 = Process(target=work)
	p2 = Process(target=work)
	p3 = Process(target=work)
	p1.start()
	p1.join()
	p2.start()
	p2.join()
	p3.start()
	p3.join()

	print("主")





