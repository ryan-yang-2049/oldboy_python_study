# -*- coding: utf-8 -*-
"""
__title__ = '协程实现生产者消费者模型3.py'
__author__ = 'yangyang'
__mtime__ = '2018.03.14'
"""
import queue
import asyncio
import random
async def produce(queue, n):
	for x in range(n):
		print('producing {}/{}'.format(x, n))
		await asyncio.sleep(random.random())
		item = str(x)
		await queue.put(item)
async def consume(queue):
	while True:
		item = await queue.get()
		print('consuming {}...'.format(item))
		await asyncio.sleep(random.random())
		queue.task_done()
async def run(n):
	q = asyncio.Queue()
	consumer = asyncio.ensure_future(consume(q))
	await produce(q,n)
	await q.join()
	consumer.cancel()

loop = asyncio.get_event_loop()
loop.run_until_complete(run(10))
loop.close()

