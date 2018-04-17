# -*- coding: utf-8 -*-
"""
__title__ = '15 multiprocessing进程池.py'
__author__ = 'yangyang'
__mtime__ = '2018.02.07'
"""

from multiprocessing import Pool
import os,time

#apply 串行，效率低。
# def task(n):
# 	print('<%s> is running'%os.getpid())
# 	time.sleep(2)
# 	print('<%s> is done'%os.getpid())
# 	return  n**2
#
# if __name__ == '__main__':
# 	p = Pool(4)              # 如果不指定大小，默认是使用cpu的个数
# 	# res1 = p.apply(task,args=(2,))              #同步提交任务    串行的执行。没有实现并发
# 	# print("res",res1)
# 	for i in range(1,9):
# 		res= p.apply(task,args=(i,))
# 		print("第%s次结果 ：%s"%(i,res))
#
# 	print("主进程",os.getpid())



def task(n):
	print('<%s> is running'%os.getpid())
	time.sleep(2)
	print('<%s> is done'%os.getpid())
	return  n**2

if __name__ == '__main__':
	p = Pool(4)              # 如果不指定大小，默认是使用cpu的个数
	obj_l = []
	for i in range(1,9):
		res= p.apply_async(task,args=(i,))     # 异步提交任务。得到的是一个对象：<multiprocessing.pool.ApplyResult object at 0x000001C88A61F4A8>
		obj_l.append(res)
		# print(res.get())   # 在这里获取结果就会变成串行，apply 就是在返回时调用了 apply_async 的get方法造成的串行。
	p.close()       # 禁止往进程池内再添加任务
	p.join()
	print("主进程",os.getpid())
	print(obj_l)
	for obj in obj_l:
		print(obj.get())        # 获取结果。





