# -*- coding: utf-8 -*-
"""
__title__ = '16 map.py'
__author__ = 'yangyang'
__mtime__ = '2018.02.08'
"""


from  concurrent.futures import ProcessPoolExecutor
import os,random,time

def task(n):
	time.sleep(random.randint(1,3))
	return n**2

if __name__ == '__main__':
	# 进程池
	start = time.time()
	pool = ProcessPoolExecutor(4)   # 如果不指认进程池的个数，默认使用CPU的个数。
	obj = pool.map(task,range(10))
	pool.shutdown()                 # 等待所有进程池里面的进程结束以后再去执行主进程
	print(list(obj))
	print("run time: %s"%(time.time()-start)) # 18.74







