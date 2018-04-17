# -*- coding: utf-8 -*-
"""
__title__ = '06 互斥锁.py'
__author__ = 'yangyang'
__mtime__ = '2018.01.29'
"""

# 互斥锁 牺牲效率，保证数据不错乱
# 互斥锁的原理就是把，并发修改同一块共享数据的操作，变成串行，数据安全。

from  multiprocessing import Process,Lock
import time
def task(name,mutex):
	mutex.acquire()
	print('%s run 1' %name)
	time.sleep(1)
	print('%s run 2' %name)
	mutex.release()

if __name__ == '__main__':
	mutex = Lock()
	for i in range(3):
		p=Process(target=task,args=("进程 %s "%i,mutex))

		p.start()


'''
不互斥的结果
0 name 1
1 name 1
2 name 1
0 name 2
1 name 2
2 name 2
0 name 3
1 name 3
2 name 3
#互斥锁的结果
0 name 1
0 name 2
0 name 3
1 name 1
1 name 2
1 name 3
2 name 1
2 name 2
2 name 3
'''




