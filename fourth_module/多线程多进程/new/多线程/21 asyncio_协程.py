# -*- coding: utf-8 -*-
"""
__title__ = '21 asyncio_协程.py'
__author__ = 'yangyang'
__mtime__ = '2018.03.14'
"""
#http://python.jobbole.com/87310/
# import time
# import asyncio
#
# now = lambda: time.time()
# #通过async关键字定义一个协程（coroutine),协程也是一种对象。
# async def do_some_work(x):
# 	print('Waiting: ', x)
#
# start = now()
# # 协程不能直接运行，需要把协程加入到事件循环（loop），由后者在适当的时候调用协程。
# coroutine = do_some_work(3)
# # 创建一个事件循环。
# loop = asyncio.get_event_loop()
# # 使用run_until_complete将协程注册到事件循环，并启动事件循环
# loop.run_until_complete(coroutine)
# print('TIME: ', now() - start)


import  asyncio
import  time

now = lambda: time.time()
# 定义一个协程对象
async def do_some_work(x):
	print("wait:",x)

start = now()

# 创建一个协程实例
coroutine = do_some_work(3)
#创建一个事件循环
loop = asyncio.get_event_loop()

#保存了协程运行后的状态，用于未来获取协程的结果。
task = loop.create_task(coroutine)
print("task111:",task)

loop.run_until_complete(task)

print("task222:",task)
print('TIME: ', now() - start)








