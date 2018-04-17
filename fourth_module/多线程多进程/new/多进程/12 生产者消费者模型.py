# -*- coding: utf-8 -*-
"""
__title__ = '12 生产者消费者模型.py'
__author__ = 'yangyang'
__mtime__ = '2018.02.07'
"""

# 队列自动解决锁的问题
# 例子：队列模拟生产者消费者模型

# from multiprocessing import Process,Queue
# import os,time,random
# # 一个生产者一个消费者
# # 这一段代码主要注意的是，生产者是put到队列，消费者是从队列get，判断结束的标志是 生产者发送None信号，
# def consumer(q):
# 	while True:
# 		res = q.get()
# 		if res is None:break        #  取数据，如果消费者收到None的值（信号），就结束该线程
# 		time.sleep(random.randint(1,3))
# 		print("\033[43m %s 消费了 %s \033[0m" % (os.getpid(), res))
#
# def producer(q):
# 	for i in range(5):
# 		time.sleep(2)
# 		res = '包子%s'%i
# 		q.put(res)
# 		print("\033[44m %s 生产了  %s \033[0m"%(os.getpid(),res))
# 	q.put(None) # 发送信号到队列里面，表示该线程（生产者）已经结束。
#
# if __name__ == '__main__':
# 	q = Queue() #存消息的容器
# 	# 生产者
# 	p1 = Process(target=producer,args=(q,))
# 	# 消费者
# 	c1 = Process(target=consumer,args=(q,))
#
# 	p1.start()
# 	c1.start()
# 	p1.join()
# 	c1.join()
# 	print("主")

# 多个生产者，多个消费者 2
# 有几个消费者，就要发送几个None的信号
from multiprocessing import Process,Queue
import os,time,random
def consumer(q):
	while True:
		res = q.get()
		if res is None:break        #  取数据，如果消费者收到None的值（信号），就结束该线程
		time.sleep(random.randint(1,3))
		print("\033[45m %s 消费了 %s \033[0m" % (os.getpid(), res))

def producer(product,q):
	for i in range(5):
		time.sleep(2)
		res = '%s%s'%(product,i)
		q.put(res)
		print("\033[44m %s 生产了  %s \033[0m"%(os.getpid(),res))
	# q.put(None) # 发送信号到队列里面，表示该线程（生产者）已经结束。

if __name__ == '__main__':
	q = Queue() #存保证的容器
	# 生产者
	p1 = Process(target=producer,args=('包子',q))
	p2 = Process(target=producer,args=('馒头',q))
	p3 = Process(target=producer,args=('烧卖',q))
	# 消费者
	c1 = Process(target=consumer,args=(q,))
	c2 = Process(target=consumer,args=(q,))
	p_l = [p1,p2,p3]
	c_l = [c1,c2]
	p1.start()
	p2.start()
	p3.start()

	c1.start()
	c2.start()

	p1.join()
	p2.join()
	p3.join()
	q.put(None)
	q.put(None)
	c1.join()
	c2.join()
	print("主")


# 生成器实现生产者消费者
# def init(func):
# 	def wrapper(*args,**kwargs):
# 		g=func(*args,**kwargs)
# 		next(g)
# 		return g
# 	return wrapper
#
# @init
# def consumer():
# 	r = ''
# 	while True:
# 		n = yield r
# 		if not n:
# 			print("not n...")
# 			return
# 		print('3==>[CONSUMER] Consuming %s...' % n)
# 		r = '200 OK'
#
# def produce(c):
# 	n = 0
# 	while n < 2:
# 		n = n + 1
# 		print('1==>[PRODUCER] Producing %s...' % n)
# 		r = c.send(n)
# 		print('2==>[PRODUCER] Consumer return: %s' % r)
# 	c.close()
#
#
# produce(consumer())


'''

'''