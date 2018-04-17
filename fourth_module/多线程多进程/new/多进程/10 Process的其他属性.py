# -*- coding: utf-8 -*-
"""
__title__ = '08  守护进程.py'
__author__ = 'ryan'
__mtime__ = '2018/2/6'
"""



from multiprocessing import Process
import os,time

# terminate 只是程序发送信号给操作系统说，要关闭某个进程，并未立马关闭
# is_alive 查看某进程是否活着,返回 True/False
# name  查看某个进程的名称
# pid 查看某个进程的PID号
def work():
	print("%s is working"%os.getpid())
	time.sleep(3)
	print("%s is done"%os.getpid())

if __name__ == '__main__':
	p1 = Process(target=work)
	p1.start()

	p1.terminate()    # 非常危险，只会回收p1 的进程，如果p1 还有子进程，那么p1 的子进程就会产生僵死进程
	time.sleep(1)
	print(p1.is_alive())
	print(p1.name)
	print(p1.pid)
	print("主")





