# -*- coding: utf-8 -*-
"""
__title__ = '06 守护线程.py'
__author__ = 'ryan'
__mtime__ = '2018/2/7'
"""

'''
#1 主进程在其代码结束后就已经算运行完毕了（守护进程在此时就被回收）,然后主进程会一直等非守护的子进程都运行完毕后回收子进程的资源(否则会产生僵尸进程)，才会结束，

#2 主线程在其他非守护线程运行完毕后才算运行完毕（守护线程在此时就被回收）。因为主线程的结束意味着进程的结束，进程整体的资源都将被回收，而进程必须保证非守护线程都运行完毕后才能结束。

'''


from threading import Thread
import time
def sayhi(name):
	print("start subthread")
	time.sleep(2)
	print('%s say hello' %name)

if __name__ == '__main__':
	t=Thread(target=sayhi,args=('egon',))
	t2=Thread(target=sayhi,args=('RYAN',))
	t.setDaemon(True) #必须在t.start()之前设置
	t.start()
	t2.start()
	print(t.is_alive())
	print('主线程')

'''
自己理解的  守护进程和守护线程：

守护进程：当主进程的代码结束以后就会结束主进程的守护进程，但是，主进程的结束会等着别的非守护进程结束而结束。
守护线程：当主线程的代码结束以后，并且主线程会等着别的子线程结束才结束，因此，守护线程会在主线程结束以后才结束，也就是守护线程会在主进程和所有的非守护线程结束以后才结束。

'''


