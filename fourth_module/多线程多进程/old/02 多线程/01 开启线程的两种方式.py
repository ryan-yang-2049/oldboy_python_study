# -*- coding: utf-8 -*-
"""
__title__ = '01 开启线程的两种方式.py'
__author__ = 'yangyang'
__mtime__ = '2018.01.31'
"""

# 方式一：
# 从资源的角度看，该程序运行的是一个主进程和一个线程
# 从程序的角度看，该程序运行的是一个主线程和一个子线程
# import time
# import random
# from threading import  Thread
#
#
# def piao(name):
# 	print('%s piaoing' %name)
# 	time.sleep(random.randrange(1,5))
# 	print('%s piao end'%name)
#
# if __name__ == '__main__':
# 	t1 = Thread(target=piao,args=('egon',))
# 	t1.start()
# 	print("主")

# 方式二：
from threading import Thread
import time

class MyThread(Thread):
    def __init__(self,name):
        super().__init__()
        self.name=name
    def run(self):
        time.sleep(2)
        print('%s say hello' % self.name)

if __name__ == '__main__':
    t = MyThread('egon')
    t.start()
    print('主线程')




