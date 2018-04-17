# -*- coding: utf-8 -*-
"""
__title__ = '08  守护进程.py'
__author__ = 'ryan'
__mtime__ = '2018/2/6'
"""

# 进程的守护进程开启方式。主进程运行完毕，守护进程直接结束，守护进程一定要在start之前定义。
# 守护进程调用的方法里面一定不能有子进程，不然会报错。

from multiprocessing import Process
import os,time

def work():
	print("%s is working"%os.getpid())
	time.sleep(20)
	print("%s is done"%os.getpid())

if __name__ == '__main__':
	p1 = Process(target=work)
	p1.daemon=True          # 进程的守护进程开启方式。主进程运行完毕，守护进程直接结束，守护进程一定要在start之前定义。
	p1.start()

	print("主")
	time.sleep(3)





