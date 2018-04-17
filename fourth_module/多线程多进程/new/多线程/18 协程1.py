# -*- coding: utf-8 -*-
"""
__title__ = '18 协程.py'
__author__ = 'yangyang'
__mtime__ = '2018.02.08'
"""

# 遇到IO 切换线程才有意义
# 单线程下实现并发
# 协程：是单线程下的并发，又称微线程，

'''
优点如下：

#1. 协程的切换开销更小，属于程序级别的切换，操作系统完全感知不到，因而更加轻量级
#2. 单线程内就可以实现并发的效果，最大限度地利用cpu
缺点如下：

#1. 协程的本质是单线程下，无法利用多核，可以是一个程序开启多个进程，每个进程内开启多个线程，每个线程内开启协程
#2. 协程指的是单个线程，因而一旦协程出现阻塞，将会阻塞整个线程

总结协程特点：
	必须在只有一个单线程里实现并发
	修改共享数据不需加锁
	用户程序里自己保存多个控制流的上下文栈
	附加：一个协程遇到IO操作自动切换到其它协程（如何实现检测IO，yield、greenlet都无法实现，就用到了gevent模块（select机制））
'''
# import gevent
# import time
#
#
# def eat(name):
# 	print('%s eat 1' % name)
# 	gevent.sleep(2)
# 	print('%s eat 2' % name)
#
#
# def play(name):
# 	print('%s play 1' % name)
# 	gevent.sleep(1)
# 	print('%s play 2' % name)
#
#
# start = time.time()
# g1 = gevent.spawn(eat, 'egon')
# g2 = gevent.spawn(play, name='egon')
# g1.join()
# g2.join()
# # 或者gevent.joinall([g1,g2])
# print('主,run time: %s' % (time.time() - start))




from gevent import monkey;monkey.patch_all()
import gevent
import time,threading

def eat(name):
	print('%s eat 1' %name)
	time.sleep(2)
	print('%s eat 2' %name)
	return 'eat'

def play(name):
	print('%s play 1' %name)
	time.sleep(1)
	print('%s play 2' %name)
	return 'play'

start=time.time()
g1=gevent.spawn(eat,'egon')
g2=gevent.spawn(play,'egon')

gevent.joinall([g1,g2])
print('主',(time.time()-start))
print(g1.value)     # 返回值
print(g2.value)













