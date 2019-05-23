# -*- coding: utf-8 -*-
"""
__title__ = '3.判断是否是函数.py'
__author__ = 'yangyang'
__mtime__ = '2018-12-15'
"""

from types import  FunctionType

def Foo():
	pass


if isinstance(Foo,FunctionType):
	print('is')








