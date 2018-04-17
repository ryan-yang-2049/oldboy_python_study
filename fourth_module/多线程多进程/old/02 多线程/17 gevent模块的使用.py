# -*- coding: utf-8 -*-
"""
__title__ = '17 gevent模块的使用.py'
__author__ = 'yangyang'
__mtime__ = '2018.02.05'
"""
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
    time.sleep(2)
    print('%s play 2' %name)
    return 'play'

start=time.time()
g1=gevent.spawn(eat,'egon')
g2=gevent.spawn(play,'egon')
# g1.join()
# g2.join()
gevent.joinall([g1,g2])
print('主',(time.time()-start))
print(g1.value)     # 返回值
print(g2.value)












