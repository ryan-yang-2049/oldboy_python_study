# -*- coding: utf-8 -*-
"""
__title__ = '04 守护线程.py'
__author__ = 'yangyang'
__mtime__ = '2018.01.31'
"""

# 主线程就代表了主进程的生命周期
#
# from threading import Thread
# import time
# def sayhi(name):
#     time.sleep(2)
#     print('%s say hello' %name)
#
# if __name__ == '__main__':
#     t1=Thread(target=sayhi,args=('egon',))
#     t1.setDaemon(True) #必须在t.start()之前设置 等价于 t.daemon=True
#
#     t2=Thread(target=sayhi,args=('alex',))
#     t1.start()
#     t2.start()
#
#     print('主线程')
#     print("t1 是否存活：%s , t2 是否存活：%s"%(t1.is_alive(),t2.is_alive()))


#
from threading import Thread
import time

def foo():
    print(123)
    time.sleep(1)
    print("end123")

def bar():
    print(456)
    time.sleep(3)
    print("end456")

if __name__ == '__main__':
    t1=Thread(target=foo)
    t2=Thread(target=bar)

    t2.daemon=True
    t1.start()
    t2.start()
    print("main-------")




