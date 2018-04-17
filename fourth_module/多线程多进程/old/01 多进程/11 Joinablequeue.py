# -*- coding: utf-8 -*-
"""
__title__ = '10 生产者消费者模型.py'
__author__ = 'yangyang'
__mtime__ = '2018.01.30'
"""
# from multiprocessing import Process,Queue
# import time
#
# def producer(q):
# 	for i in range(5):
# 		res = "包子%s"%i
# 		time.sleep(0.5)
# 		print("生产者生产了: %s"%res)
# 		q.put(res)
#
# def consumer(q):
# 	while True:
# 		res = q.get()
# 		if res is None:break
# 		time.sleep(1)
# 		print("消费者吃了: %s"%res)
#
#
# if __name__ == '__main__':
# 	# 容器
# 	q = Queue()
#
# 	# 生产者们
# 	p1 = Process(target=producer,args=(q,))
# 	p2 = Process(target=producer,args=(q,))
# 	p3 = Process(target=producer,args=(q,))
#
#
# 	# 消费者们
# 	c1 = Process(target=consumer,args=(q,))
# 	c2 = Process(target=consumer,args=(q,))
#
# 	p1.start()
# 	p2.start()
# 	p3.start()
#
# 	c1.start()
# 	c2.start()
#
# 	p1.join()
# 	p2.join()
# 	p3.join()
# 	q.put(None)
# 	q.put(None)
# 	print("主")

# JoinableQueue 实现生产者和消费者
from multiprocessing import Process,JoinableQueue
import time,random,os
def consumer(q,name):
    while True:
        res=q.get()
        time.sleep(random.randint(1,3))
        print('\033[43m%s 吃 %s\033[0m' %(name,res))
        q.task_done() #发送信号给q.join()，说明已经从队列中取走一个数据并处理完毕了

def producer(q,name,food):
    for i in range(3):
        time.sleep(random.randint(1,3))
        res='%s%s' %(food,i)
        q.put(res)
        print('\033[45m%s 生产了 %s\033[0m' %(name,res))
    q.join() #等到消费者把自己放入队列中的所有的数据都取走之后，生产者才结束

if __name__ == '__main__':
    q=JoinableQueue() #使用JoinableQueue()

    #生产者们:即厨师们
    p1=Process(target=producer,args=(q,'egon1','包子'))
    p2=Process(target=producer,args=(q,'egon2','骨头'))
    p3=Process(target=producer,args=(q,'egon3','泔水'))

    #消费者们:即吃货们
    c1=Process(target=consumer,args=(q,'alex1'))
    c2=Process(target=consumer,args=(q,'alex2'))
    c1.daemon=True
    c2.daemon=True

    #开始
    p1.start()
    p2.start()
    p3.start()
    c1.start()
    c2.start()

    p1.join()
    p2.join()
    p3.join()

