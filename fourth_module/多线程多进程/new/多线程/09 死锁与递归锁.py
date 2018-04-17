# -*- coding: utf-8 -*-
"""
__title__ = '09 死锁与递归锁.py'
__author__ = 'yangyang'
__mtime__ = '2018.02.08'
"""

# 死锁： 是指两个或两个以上的进程或线程在执行过程中，因争夺资源而造成的一种互相等待的现象，若无外力作用，它们都将无法推进下去。此时称系统处于死锁状态或系统产生了死锁，这些永远在互相等待的进程称为死锁进程，如下就是死锁

# 造成下面的原因是，两个线程在对方身上都有需要的锁，因此 造成了死锁。
from threading import Thread,Lock
import time
mutexA=Lock()
mutexB=Lock()

class MyThread(Thread):
    def run(self):
        self.func1()
        self.func2()
    def func1(self):
        mutexA.acquire()
        print('\033[41m%s 拿到A锁\033[0m' %self.name)

        mutexB.acquire()
        print('\033[42m%s 拿到B锁\033[0m' %self.name)
        mutexB.release()

        mutexA.release()

    def func2(self):
        mutexB.acquire()
        print('\033[43m%s 拿到B锁\033[0m' %self.name)
        time.sleep(2)

        mutexA.acquire()
        print('\033[44m%s 拿到A锁\033[0m' %self.name)
        mutexA.release()

        mutexB.release()

if __name__ == '__main__':
    for i in range(10):
        t=MyThread()
        t.start()

# 递归锁：可以连续acquire多次，每次acquire一次计数器+1，当release一次计数器-1，因此，只要递归锁的计数不为0，就不能被其他线程抢到。
#
# from threading import Thread,RLock
# import time
# mutexA=RLock() # 创建递归锁对象
# print("mutexA",mutexA)
#
#
# class MyThread(Thread):
#     def run(self):
#         self.func1()
#         self.func2()
#     def func1(self):
#         mutexA.acquire()
#         print('\033[41m%s 拿到A锁\033[0m' %self.name)
#         mutexA.acquire()
#         print('\033[42m%s 拿到B锁\033[0m' %self.name)
#         mutexA.release()
#         mutexA.release()
#
#     def func2(self):
#         mutexA.acquire()
#         print('\033[43m%s 拿到B锁\033[0m' %self.name)
#         time.sleep(2)
#
#         mutexA.acquire()
#         print('\033[44m%s 拿到A锁\033[0m' %self.name)
#         mutexA.release()
#         mutexA.release()
#
# if __name__ == '__main__':
#     for i in range(10):
#         t=MyThread()
#         t.start()









