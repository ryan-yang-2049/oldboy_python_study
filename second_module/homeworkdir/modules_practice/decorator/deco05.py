# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'yangyang'
__mtime__ = '2018.01.02'
"""
from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(func.__name__, func.__doc__, 'call decorator')
        return func(*args, **kwargs)

    return wrapper


@decorator
def show():
    """show test """
    print('......')


show()
print(show.__name__)  # show
print(show.__doc__) # show test

# res:
# show  show test  call decorator
# ......
# show
# show test