# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'yangyang'
__mtime__ = '2018.01.04'
"""
def something():
    result = []
    for i in range(1,10):
        result.append(i)
    return result


def iter_something():
    for i in range(1,10):
        yield i

# res = something()
# print(res)

res02 = iter_something()
# print(next(res02))
# print(next(res02))
# print(next(res02))
# print(next(res02))
# print(next(res02))
while True:
    res = next(res02)
    if res == 3:
        print("aaa")
        break
















