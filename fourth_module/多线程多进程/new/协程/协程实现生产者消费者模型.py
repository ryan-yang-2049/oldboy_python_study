# -*- coding: utf-8 -*-
"""
__title__ = '协程实现生产者消费者模型.py'
__author__ = 'yangyang'
__mtime__ = '2018.03.14'
"""

import asyncio
import os,time,random
import queue
async def consumer(q):
	while True:
		res = q.get()
		if res is None:break
		await asyncio.sleep(random.randint(1,3))
		print("\033[43m %s 消费了 %s \033[0m" % (os.getpid(), res))


async def producer(q):
	for i in range(5):
		print('x:',i)
		await asyncio.sleep(2)
		res = '包子%s'%i
		q.put(res)
		print("\033[44m %s 生产了  %s \033[0m" % (os.getpid(), res))
	q.put(None)


if __name__ == '__main__':
	q = queue.Queue()

	loop = asyncio.get_event_loop()
	coros = [producer(q),consumer(q)]
	futus = asyncio.ensure_future(asyncio.gather(*coros))

	loop.run_until_complete(futus)

	loop.close()








