# -*- coding: utf-8 -*-
"""
__title__ = '07 join方法.py'
__author__ = 'yangyang'
__mtime__ = '2018.02.08'
"""

# from threading import Thread,currentThread
# import time
#
# def work():
# 	print("%s is running"%currentThread().getName())
# 	time.sleep(3)
# 	print("%s is done"%currentThread().getName())
#
# if __name__ == '__main__':
# 	start = time.time()
# 	t_list = []
# 	for i in range(10):
# 		t=Thread(target=work)
# 		t_list.append(t)
# 		t.start()
# 	for t in  t_list:
# 		t.join()
#
# 	print("主,total time: %s"%(time.time()-start))


from threading import Thread,currentThread,Lock
import time

n=100
def work(mutex):
	time.sleep(2)
	global n
	mutex.acquire()
	temp = n
	time.sleep(1)
	n = temp - 10
	mutex.release()

if __name__ == '__main__':
	mutex = Lock()
	start = time.time()
	t_list = []
	for i in range(10):
		t=Thread(target=work,args=(mutex,))
		t_list.append(t)
		t.start()
		# t.join()
	for t in  t_list:
		t.join()

	print("主,total time: %s,n:[%s]"%(time.time()-start,n))

