# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'yangyang'
__mtime__ = '2018.01.02'
"""
import logging

def use_logging(level):
    def decorator(func):
        def wrapper(*args,**kwargs):
            if level == "warn":
                logging.warning("%s is running"%func.__name__)
            return func(*args)
        return wrapper
    return decorator

@use_logging(level="warn")
def foo(name='foo'):
    print("i am %s"%name)

foo()


# res:
# i am foo
# WARNING:root:foo is running