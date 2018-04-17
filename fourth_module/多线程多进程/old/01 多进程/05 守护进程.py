# -*- coding: utf-8 -*-
"""
__title__ = '05 守护进程.py'
__author__ = 'yangyang'
__mtime__ = '2018.01.29'
"""
'''
关于守护进程需要强调两点：
其一：守护进程会在主进程代码执行结束后就终止
其二：守护进程内无法再开启子进程,否则抛出异常：AssertionError: daemonic processes are not allowed to have children
'''
# from multiprocessing import  Process
# import time
# def task(name,n):
#     print('%s is running'%name)
#     time.sleep(n)
#     print('%s is done' % name)
#
# if __name__ == '__main__':
#     p = Process(target=task,args=('子进程1',6))
#     p2 = Process(target=task,args=('子进程2',6))
#     p.daemon = True
#     p2.daemon = True
#     p.start()
#     p.join()
#     p2.start()
#     print("主")
#     time.sleep(5)
#     print("主over")


#验证上面观点二：抛出异常
# from multiprocessing import  Process
# import time
# def task(name):
# 	print('%s is running'%name)
# 	time.sleep(2)
# 	p=Process(target=time.sleep,args=(3,))
# 	p.start()
#
#
# if __name__ == '__main__':
# 	p = Process(target=task,args=('子进程1',))
# 	p.daemon = True
# 	p.start()
# 	p.join()
#
# 	print("主")

# 练习题：
from multiprocessing import Process
import time

def foo():
    print(123)
    time.sleep(10)
    print("end123")

def bar():
    print(456)
    # time.sleep(1)
    print("end456")

if __name__ == '__main__':
    p1=Process(target=foo)
    p2=Process(target=bar)

    # p1.join()

    p1.daemon=True
    p1.start()
    p2.start()

    p2.join()
    print("main-------")






