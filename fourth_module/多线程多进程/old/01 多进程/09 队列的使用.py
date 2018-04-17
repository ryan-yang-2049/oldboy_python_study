# -*- coding: utf-8 -*-
"""
__title__ = '09 队列的使用.py'
__author__ = 'yangyang'
__mtime__ = '2018.01.29'
"""
# 队列：精简的小数据
# 队列：先进先出，栈：先进后出

from multiprocessing import Process,Queue
q=Queue(3)
# put 放入消息队列，get 获取消息队列里面的内容。
#put ,get ,put_nowait,get_nowait,full,empty
q.put(1)
q.put(2)
q.put(3)
print(q.full()) #满了
q.put(4) #再放就阻塞住了

print(q.get())
print(q.get())
print(q.get())
print(q.empty()) #空了
# print(q.get()) #再取就阻塞住了
