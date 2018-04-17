# -*- coding: utf-8 -*-
"""
__title__ = '13 JoinableQueue.py'
__author__ = 'yangyang'
__mtime__ = '2018.02.07'
"""

# 多个生产者，多个消费者
from multiprocessing import Process,JoinableQueue
import os, time, random
def consumer(q):
	while True:
		res = q.get()
		time.sleep(random.randint(1, 3))
		print("\033[45m %s 消费了 %s \033[0m" % (os.getpid(), res))
		q.task_done()

def producer(product, q):
	for i in range(3):
		time.sleep(2)
		res = '%s%s' % (product, i)
		q.put(res)
		print("\033[44m %s 生产了  %s \033[0m" % (os.getpid(), res))
	q.join()

if __name__ == '__main__':
	q = JoinableQueue()  # 存消息的容器,相对于Queue多了一个  task_done 的方法

	# 生产者
	p1 = Process(target=producer, args=('包子', q))
	p2 = Process(target=producer, args=('馒头', q))
	p3 = Process(target=producer, args=('烧卖', q))
	# 消费者
	c1 = Process(target=consumer, args=(q,))
	c2 = Process(target=consumer, args=(q,))
	c1.daemon = True
	c2.daemon = True

	p_l = [p1, p2, p3,]
	c_l = [c1, c2]
	for p in p_l:
		p.start()
	c1.start()
	c2.start()
	for p in p_l:
		p.join()

	print("主")








