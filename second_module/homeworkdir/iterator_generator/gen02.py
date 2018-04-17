# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'yangyang'
__mtime__ = '2018.01.04'
"""
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            print("not n...")
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    f = c.send(None)
    print('[PRODUCER] Consumer first return: %s' % f)
    n = 0
    while n < 2:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)