# -*- coding: utf-8 -*-
"""
__title__ = '11 进程Queue.py'
__author__ = 'ryan'
__mtime__ = '2018/2/6'
"""

# 队列：先进先出
# 队列：放在内存，相当于共享的内存。自动加锁，解决了锁的问题。
# 队列：生产者消费者模型必须要知道的知识点。

from multiprocessing import Process,Queue

q = Queue(3)    # 队列的大小，可以不指定大小(相当于无限大，但实际大小跟内存有关)

# 存数据
q.put({'name':'ryan','age':18}) # 放数据，可以放任意python的数据
q.put(['ryan',18])
q.put((1,2,3))
# q.put('str')   # 因为q的大小为3个，因此放这个的时候，程序会卡着
# q.put('str',block=False,timeout=5)   # 默认 block=True ，当队列满了就抛出异常  queue.Full

# 取数据
print(q.get())
print(q.get())
print(q.get())
# print(q.get()) # 同放数据一样，q 的大小为3，当已经取了三个以后，没有在put数据，也会继续卡着
# print(q.get(block=False,timeout=5)) # 默认block=True，如果timeout（5s）以内还没有内容就抛出异常 queue.Empty

q.get_nowait()   # 相当于 q.get(block=False)，如果队列被取完了，也会抛出异常 queue.Empty