# -*- coding: utf-8 -*-
"""
__title__ = '03 Process对象的其他属性或方法.py'
__author__ = 'yangyang'
__mtime__ = '2018.01.29'
"""
#并发执行
# from multiprocessing import  Process
# import time,os
# def task(name,n):
# 	print('%s is running，pid is %s'%(name,os.getpid()))
# 	time.sleep(n)
# 	print('%s is done,parent pid is ==> %s'%(name,os.getppid()))
#
#
#
# if __name__ == '__main__':
# 	start = time.time()
# 	p1=Process(target=task,args=('子进程1',2,))
# 	p2=Process(target=task,args=('子进程2',5,))
# 	p3=Process(target=task,args=('子进程3',3))
# 	process_list = [p1,p2,p3]
# 	for i in process_list:
# 		i.start()
#
# 	for pj in process_list:
# 		pj.join()
#
# 	print('主',time.time()-start)


# 串行执行
# from multiprocessing import  Process
# import time,os
# def task(name,n):
# 	print('%s is running，pid is %s'%(name,os.getpid()))
# 	time.sleep(n)
# 	print('%s is done,parent pid is ==> %s'%(name,os.getppid()))
#
#
#
# if __name__ == '__main__':
# 	start = time.time()
# 	p1=Process(target=task,args=('子进程1',5,))
# 	p2=Process(target=task,args=('子进程2',3,))
# 	p3=Process(target=task,args=('子进程3',2))
#
# 	p1.start()
# 	p1.join()
# 	p2.start()
# 	p2.join()
# 	p3.start()
# 	p3.join()
# 	print('主',time.time()-start)


# 了解的属性和方法
# is_alive：进程是否存活
# terminate：杀死进程,发送信号给操作系统，操作系统需要一段时间才能够杀死进程。
# name:查看进程的名字，可以在创建对象的时候指定进程名称。
from multiprocessing import  Process
import time,os
def task(name):
	print('%s is running，pid is %s'%(name,os.getpid()))
	time.sleep(3)
	print('%s is done,parent pid is ==> %s'%(name,os.getppid()))



if __name__ == '__main__':
	# p=Process(target=task,args=('子进程1',))
	# p.start()
	# p.join()
	# print('主',os.getpid(),os.getppid())
	# print(p.pid)
	# print(p.is_alive())
	p=Process(target=task,name='myprocess-1',args=('子进程1',))
	p.start()
	p.terminate()       # 杀死进程,发送信号给操作系统，操作系统需要一段时间才能够杀死进程。
	time.sleep(3)
	print(p.is_alive())
	print('主')
	print(p.name)





