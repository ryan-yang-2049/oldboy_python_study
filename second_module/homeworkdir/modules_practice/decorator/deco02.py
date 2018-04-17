# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'yangyang'
__mtime__ = '2018.01.02'
"""
import logging
def use_logging(func):
    def wrapper(*args,**kwargs):
        logging.warning("%s is running"%func.__name__)
        return func(*args,**kwargs)
    return wrapper

@use_logging
def bar():
    print("i am bar")

@use_logging
def foo():
    print("i am foo")

bar()


