# -*- coding: utf-8 -*-
"""
__title__ = '05 练习题.py'
__author__ = 'yangyang'
__mtime__ = '2018.03.08'
"""

# from multiprocessing import Process
# import time
# import random
#
# def task(n):
#     time.sleep(random.randint(1,3))
#     print('-------->%s' %n)
#
# if __name__ == '__main__':
#     p1=Process(target=task,args=(1,))
#     p2=Process(target=task,args=(2,))
#     p3=Process(target=task,args=(3,))
#
#     p1.start()
#     p1.join()
#     p2.start()
#     p2.join()
#     p3.start()
#     p3.join()
#     print('-------->4')

from multiprocessing import Process
import time

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
    p1=Process(target=foo)
    p2=Process(target=bar)

    p1.daemon=True
    p1.start()
    p2.start()
    print("main-------")






