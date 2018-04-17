#coding:utf-8


# 进程池：ProcessPoolExecutor，线程池：ThreadPoolExecutor 他们的接口一模一样，学会一个另一个自然会用，唯一需要知道是，什么时候用线程池，什么时候用进程池。
# 进程池和线程池的本质还是开进程或者开线程
# 进程：计算密集型，想用多核用进程
# 线程：I/O密集型，用多线程，例如：socket

# 线程池/进程池：池对数目加以限制，保证机器以一个可承受的范围，以一个健康的状态保证程序的进行。

# 进程池
# from  concurrent.futures import ProcessPoolExecutor
# import os,random,time
#
# def task(arg):
# 	print('name: %s,PID: %s run'%(arg,os.getpid()))
# 	time.sleep(random.randint(1,3))
#
# if __name__ == '__main__':
# 	# 进程池
# 	print("pool before")
# 	pool = ProcessPoolExecutor(4)   # 如果不指认进程池的个数，默认使用CPU的个数。
# 	for i in range(10):
# 		pool.submit(task,'egon%s'%i) # 提交任务的方式叫异步调用。提交完任务，不用再等着任务提交执行结果的返回。
# 	pool.shutdown()                 # 等待所有进程池里面的进程结束以后再去执行主进程
# 	print("主")


# 线程池
from  concurrent.futures import ThreadPoolExecutor
import os,random,time
from threading import  currentThread

def task():
	print('name: %s,PID: %s run'%(currentThread().getName(),os.getpid()))
	time.sleep(random.randint(1,3))

if __name__ == '__main__':
	pool = ThreadPoolExecutor(5)  # 如果不指认进程池的个数，默认使用CPU的个数。
	for i in range(10):
		pool.submit(task) # 提交任务的方式叫异步调用。提交完任务，不用再等着任务提交执行结果的返回。
	pool.shutdown(wait=True)                 # 等待所有线程池里面的进程结束以后再去执行主进程, 默认值为True
	print("主")


# 并行
# from  concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
# import time,random,os
# from threading import  currentThread
# def task(n):
# 	print("%s:%s is running"%(currentThread().getName(),os.getpid()))
# 	time.sleep(random.randint(1,3))
# 	return n**2
#
# if __name__ == '__main__':
# 	start = time.time()
# 	# p =  ProcessPoolExecutor()
# 	p =  ThreadPoolExecutor()   #默认线程个数为：cpu个数 * 5
# 	l = []
# 	for i in range(22):
# 		obj = p.submit(task,i)
# 		l.append(obj)
# 	p.shutdown()
# 	print([obj.result() for obj in l])
# 	stop = time.time()
# 	print("一共运行了 %s"%(stop-start))


# 进程池串行
# from  concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
# import time,random,os
# from threading import  currentThread
# def task(n):
# 	print("%s:%s is running"%(currentThread().getName(),os.getpid()))
# 	time.sleep(random.randint(1,3))
# 	return n**2
#
# if __name__ == '__main__':
# 	start = time.time()
# 	p =  ProcessPoolExecutor()
# 	# p =  ThreadPoolExecutor()   #默认线程个数为：cpu个数 * 5
# 	for i in range(10):
# 		obj = p.submit(task,i).result()
# 		print(obj)
# 	stop = time.time()
# 	print("一共运行了 %s"%(stop-start))























