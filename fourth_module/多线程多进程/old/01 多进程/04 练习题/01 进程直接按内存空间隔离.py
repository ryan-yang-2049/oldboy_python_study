# -*- coding: utf-8 -*-
"""
__title__ = '01 进程直接按内存空间隔离.py'
__author__ = 'yangyang'
__mtime__ = '2018.01.29'
"""

from multiprocessing import Process

n=100 #在windows系统中应该把全局变量定义在if __name__ == '__main__'之上就可以了

def work():
    global n
    n=0
    print('子进程内: ',n)


if __name__ == '__main__':
    p=Process(target=work)
    p.start()
    p.join()
    print('主进程内: ',n)









