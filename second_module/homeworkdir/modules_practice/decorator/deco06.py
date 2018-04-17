# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'yangyang'
__mtime__ = '2018.01.02'
"""
def decorator(func):
    def wrapper(*args, **kwargs):
        '''wrapper test'''
        print(func.__name__, func.__doc__, 'call decorator')
        return func(*args, **kwargs)

    return wrapper


@decorator
def show():
    """ show test """
    print('......')


show()
print(show.__name__)  # wrapper
print(show.__doc__) # None


# res:
# show  show test  call decorator
# ......
# wrapper
# wrapper test
