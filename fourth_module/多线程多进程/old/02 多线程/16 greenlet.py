# -*- coding: utf-8 -*-
"""
__title__ = '16 greenlet.py'
__author__ = 'yangyang'
__mtime__ = '2018.02.05'
"""

from greenlet import greenlet
import time
def eat(name):
    print('%s eat 1' %name)
    time.sleep(10)
    g2.switch('egon')
    print('%s eat 2' %name)
    g2.switch()
def play(name):
    print('%s play 1' %name)
    g1.switch()
    print('%s play 2' %name)

g1=greenlet(eat)
g2=greenlet(play)

g1.switch('egon')#可以在第一次switch时传入参数，以后都不需要










