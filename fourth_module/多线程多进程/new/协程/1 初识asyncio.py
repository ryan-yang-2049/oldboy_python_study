# -*- coding: utf-8 -*-
"""
__title__ = '1 初识asyncio.py'
__author__ = 'yangyang'
__mtime__ = '2018.03.14'
"""
#1 定义一个协程函数
# import asyncio
# # async def 来定义一个协程函数(do_some_work)
# async def do_some_work(x):pass
# #判断是否是协程函数
# print(asyncio.iscoroutinefunction(do_some_work))

#2 运行一个简单的协程
# 协程什么都没做，我们让它睡眠几秒，以模拟实际的工作量
# 在解释 await 之前，有必要说明一下协程可以做哪些事。协程可以：
#
# * 等待一个 future 结束
# * 等待另一个协程（产生一个结果，或引发一个异常）
# * 产生一个结果给正在等它的协程
# * 引发一个异常给正在等它的协程
# asyncio.sleep 也是一个协程，所以 await asyncio.sleep(x) 就是等待另一个协程。

# import asyncio
#
# async def do_some_work(x):
# 	print("waiting:",x)
# 	await asyncio.sleep(x)
# print(asyncio.iscoroutine(do_some_work(3))) #True
# '''
# 抛出异常：
# D:/gitcode/oldboy_python_study/fourth_module/多线程多进程/new/协程/1 初识asyncio.py:29: RuntimeWarning: coroutine 'do_some_work' was never awaited
#   print(asyncio.iscoroutine(do_some_work(3)))
#
# 要让这个协程对象运行的话，有两种方式：
# * 在另一个已经运行的协程中用 `await` 等待它
# * 通过 `ensure_future` 函数计划它的执行
#
# 简单来说，只有 loop 运行了，协程才可能运行。
# 下面先拿到当前线程缺省的 loop ，然后把协程对象交给 loop.run_until_complete，协程对象随后会在 loop 里得到运行。
#
# '''
# import asyncio
#
# async def do_some_work(x):
# 	print("waiting:",x)
# 	await asyncio.sleep(x)
# loop = asyncio.get_event_loop()
# loop.run_until_complete(do_some_work(3)) # loop.run_until_complete()
# '''
# run_until_complete 是一个阻塞（blocking）调用，直到协程运行结束，它才返回。这一点从函数名不难看出。
# run_until_complete 的参数是一个 future，但是我们这里传给它的却是协程对象，之所以能这样，是因为它在内部做了检查，通过 ensure_future 函数把协程对象包装（wrap）成了 future。所以，我们可以写得更明显一些：
# loop.run_until_complete(asyncio.ensure_future(do_some_work(3)))
#
# '''
'''
重新看下回调函数
'''
# 3 回调
#假如协程是一个 IO 的读操作，等它读完数据后，我们希望得到通知，以便下一步数据的处理。这一需求可以通过往 future 添加回调来实现。
# 注意回调函数必须和 future 搭配使用。
# import asyncio
#
# async def do_some_work(x):
# 	print("waiting:",x)
# 	await asyncio.sleep(x)
#
#
# def done_callback(futu):
# 	print('done')
#
# loop = asyncio.get_event_loop()
# # loop.run_until_complete(do_some_work(3))
# futu = asyncio.ensure_future(do_some_work(3))
# futu.add_done_callback(done_callback)
#
# loop.run_until_complete(futu)


# 4 运行多个协程的三种方法
# 实际项目中，往往有多个协程，同时在一个 loop 里运行。为了把多个协程交给 loop，需要借助 asyncio.gather 函数。

# import asyncio
# import time
# async def do_some_work(x):
# 	print("waiting:",x)
# 	await asyncio.sleep(x)
#
#
# def done_callback(futu):
# 	print('done')
#
# now = lambda:time.time()
# start = now()
# loop = asyncio.get_event_loop()
# # loop.run_until_complete(do_some_work(3))
# #第一种方法：把全部协程写到 asyncio.gather里面
# # futu = asyncio.ensure_future(asyncio.gather(do_some_work(3),do_some_work(2)))
# # futu.add_done_callback(done_callback)
# # loop.run_until_complete(futu)
# #第一种方法如果不使用回调函数，还可以如下写
# # loop.run_until_complete(asyncio.gather(do_some_work(3),do_some_work(2)))
#
# # 第二种方法：可以把多个协程写到一个列表里面
# coros = [do_some_work(3),do_some_work(2),do_some_work(5)]
# futu = asyncio.ensure_future(asyncio.gather(*coros))
# futu.add_done_callback(done_callback)
# loop.run_until_complete(futu)
# # 如果不使用回调函数，也可以像第一种方法一样。
#
# # 第三种方法
# # futus = [asyncio.ensure_future(do_some_work(1)),
# #              asyncio.ensure_future(do_some_work(3))]
# #
# # loop.run_until_complete(asyncio.gather(*futus))
#
# print("run time：",now()- start) # 以上的多个协程都是并发运行的，因此，耗时是运行时间最长的协程的时间。

# gather 起聚合的作用，把多个 futures 包装成单个 future，因为 loop.run_until_complete 只接受单个 future。

# 5 run_until_complete 和 run_forever
# 我们一直通过 run_until_complete 来运行 loop ，等到 future 完成，run_until_complete 也就返回了。

# 当使用 run_forever 要在协程函数里面去停止，因为这样表示的结束该协程的循环事件，并不是去停止全局的循环事件。
# import  asyncio
#
# async def do_some_work(loop,x):
# 	print("waiting:",x)
# 	await asyncio.sleep(x)
# 	print(x,":DONE")
# 	loop.stop()
#
# loop = asyncio.get_event_loop()
# coro = do_some_work(loop,3)
# asyncio.ensure_future(coro)
# loop.run_forever()
# print("over")

# 6 run_forever 运行多个协程
# import  asyncio
#
# async def do_some_work(loop,x):
# 	print("waiting:",x)
# 	await asyncio.sleep(x)
# 	print(x,":DONE")
# 	loop.stop()
#
# loop = asyncio.get_event_loop()
# coros = [do_some_work(loop,3),do_some_work(loop,2)]
# asyncio.ensure_future(asyncio.gather(*coros))
# loop.run_forever()
# print("over")
'''
从结果可以看出，do_some_work(loop,2) 这个协程运行结束，loop就被全局结束了，但是 do_some_work(loop,3) 并没有结束。要解决这个问题，就要使用回调函数去解决。当然，使用回调函数，要搭配gather的方法。
waiting: 3
waiting: 2
2 :DONE
over
'''
# 解决方法
# functools 去学习。
# import  asyncio
# import functools
#
# async def do_some_work(x):
# 	print("waiting:",x)
# 	await asyncio.sleep(x)
# 	print(x,":DONE")
#
# def done_callback(loop,futu):
# 	loop.stop()
#
#
# loop = asyncio.get_event_loop()
# coros = [do_some_work(3),do_some_work(2)]
# futu = asyncio.ensure_future(asyncio.gather(*coros))
# futu.add_done_callback(functools.partial(done_callback,loop))
# loop.run_forever()
#
# # 其实这基本上就是 run_until_complete 的实现了，run_until_complete 在内部也是调用 run_forever。


# 7 close loop
# 简单来说，loop 只要不关闭，就还可以再运行。
# loop.run_until_complete(do_some_work(loop, 1))
# loop.close()
# loop.run_until_complete(do_some_work(loop, 3))  # 此处异常
# #建议调用 loop.close，以彻底清理 loop 对象防止误用。





