# -*- coding: utf-8 -*-
"""
__title__ = '02 开启进程的两种方式.py'
__author__ = 'yangyang'
__mtime__ = '2018.02.06'
"""
# 方式一
from multiprocessing import Process
import time,random
import os

def piao(name,n):
	print("pid:%s,PPID:%s"%(os.getpid(),os.getppid()))
	print("%s is piaoing"%name)
	time.sleep(n)
	print("%s is piao end"%name)

if __name__ == '__main__':
	# windows下开启子进程的方法必须写到 __main__ 下面
	p1 = Process(target=piao,kwargs={'name':'alex','n':random.randint(1,3)})
	p2 = Process(target=piao,kwargs={'name':'curry','n':random.randint(1,3)})
	p3 = Process(target=piao,kwargs={'name':'jams','n':random.randint(1,3)})
	# p = Process(target=piao,args=('alex',random.randint(1,3),))
	p1.start()
	p2.start()
	p3.start()
	print("主,PID:%s"%os.getpid())


# class MyProcess(Process):
# 	def __init__(self,name):
# 		super().__init__()
# 		self.name = name
#
# 	# 自己定义进程类一定要使用run命名方法名称
# 	def run(self):
# 		print("pid:%s,PPID:%s"%(os.getpid(),os.getppid()))
# 		print("%s is piaoing"%self.name)
# 		time.sleep(random.randint(1,3))
# 		print("%s is piao end"%self.name)
#
#
# if __name__ == '__main__':
# 	p1 = MyProcess('alex')
# 	p2 = MyProcess('egon')
# 	p1.start()
# 	p2.start()



