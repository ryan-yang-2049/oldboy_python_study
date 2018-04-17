# -*- coding: utf-8 -*-
"""
__title__ = '14 进程池和线程池.py'
__author__ = 'yangyang'
__mtime__ = '2018.02.08'
"""


# 线程池/进程池：池对数目加以限制，保证机器以一个可承受的范围，以一个健康的状态保证程序的进行。

# # 进程池
# from  concurrent.futures import ProcessPoolExecutor
# import os,random,time
#
# def task(arg,n):
# 	print('name: %s,PID: %s run'%(arg,os.getpid()))
# 	time.sleep(random.randint(1,3))
# 	return n**2
#
# if __name__ == '__main__':
# 	# 进程池
# 	start = time.time()
# 	pool = ProcessPoolExecutor(4)   # 如果不指认进程池的个数，默认使用CPU的个数。
# 	p_list = []
# 	for i in range(10):
# 		p=pool.submit(task,'egon%s'%i,i)# 提交任务的方式叫异步调用。提交完任务，不用再等着任务提交执行结果的返回。
# 		print("submit的对象：",p)       # <Future at 0x1d138564cc0 state=running>
# 		p_list.append(p)
# 	pool.shutdown()                 # 等待所有进程池里面的进程结束以后再去执行主进程
# 	print("主")
# 	print([obj.result() for obj in p_list])
# 	print("run time: %s"%(time.time()-start))   # 运行时间： 7.62


#
# from  concurrent.futures import ProcessPoolExecutor
# import os,random,time
#
# def task(arg,n):
# 	print('name: %s,PID: %s run'%(arg,os.getpid()))
# 	time.sleep(random.randint(1,3))
# 	return n**2
#
# if __name__ == '__main__':
# 	# 进程池
# 	start = time.time()
# 	pool = ProcessPoolExecutor(4)   # 如果不指认进程池的个数，默认使用CPU的个数。
# 	p_list = []
# 	for i in range(10):
# 		p=pool.submit(task,'egon%s'%i,i).result()# 提交任务的方式叫异步调用。提交完任务，不用再等着任务提交执行结果的返回。
# 		# 此时 p 直接result，那么这个进程池就变成了串行。
# 		p_list.append(p)
# 	pool.shutdown()                 # 等待所有进程池里面的进程结束以后再去执行主进程
# 	print("主")
# 	print(p_list)
# 	# print([obj.result() for obj in p_list])
# 	print("run time: %s"%(time.time()-start)) # 18.74




# 线程池
from  concurrent.futures import ThreadPoolExecutor
import os,random,time

def task(arg,n):
	print('name: %s,PID: %s run'%(arg,os.getpid()))
	time.sleep(random.randint(1,3))
	return n**2

if __name__ == '__main__':
	# 进程池
	start = time.time()
	pool = ThreadPoolExecutor()             # 最大线程池，默认为： cpu个数 * 5
	p_list = []
	for i in range(22):
		p=pool.submit(task,'egon%s'%i,i)# 提交任务的方式叫异步调用。提交完任务，不用再等着任务提交执行结果的返回。
		# print("submit的对象：",p)       # <Future at 0x1d138564cc0 state=running>
		p_list.append(p)
	pool.shutdown()                 # 等待所有进程池里面的进程结束以后再去执行主进程
	print("主")
	print([obj.result() for obj in p_list])
	print("run time: %s"%(time.time()-start))   # 运行时间：3.005432605743408




