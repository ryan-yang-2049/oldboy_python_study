# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'yangyang'
__mtime__ = '2018.01.04'
"""
def d():
    global m
    global n
    while True:
        print ("send() will here... test generator send()")
        m = yield 5
        print ("send input is m : %s" % m)
        n = yield 6
        print ("test generator send2")

g_obj = d()
print ("===============g_obj test d: %s" % g_obj)
s_return1 = g_obj.send(None)
s_return2 = g_obj.send("send twice")
s_return3 = g_obj.send("thrid twice")
print("the next send input will be the result of last yield, just like m is : %s, s_return1 is : %s, s_return2 is : %s" % (m, s_return1, s_return2))
print("not next send so n is undefind, n is : %s" % n)