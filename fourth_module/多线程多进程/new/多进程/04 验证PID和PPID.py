# -*- coding: utf-8 -*-
"""
__title__ = '04 验证PID和PPID.py'
__author__ = 'yangyang'
__mtime__ = '2018.02.06'
"""
# 方式一
from multiprocessing import Process,current_process
import time,random
import os

def piao(name,n):

	print("%s is piaoing"%name)
	time.sleep(n)
	print("%s , PID:%s   PPID:%s" % (current_process().name,os.getpid(), os.getppid()))

if __name__ == '__main__':
	# windows下开启子进程的方法必须写到 __main__ 下面
	p1 = Process(target=piao,name='subprocess-1',kwargs={'name':'alex','n':random.randint(3,7)})
	p2 = Process(target=piao,name='subprocess-2',kwargs={'name':'curry','n':random.randint(2,5)})
	p3 = Process(target=piao,name='subprocess-3',kwargs={'name':'jams','n':random.randint(1,4)})
	# p = Process(target=piao,args=('alex',random.randint(1,3),))
	p1.start()
	p2.start()
	p3.start()
	print("主进程,PID:%s   PPID：%s"%(os.getpid(),os.getppid()))

'''
主进程,PID:458964   PPID：458028
jams is piaoing
curry is piaoing
alex is piaoing
subprocess-3 , PID:460424   PPID:458964
subprocess-1 , PID:452104   PPID:458964
subprocess-2 , PID:459056   PPID:458964
'''

