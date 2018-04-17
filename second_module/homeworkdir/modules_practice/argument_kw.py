# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'yangyang'
__mtime__ = '2018.01.02'
"""



dic = {'k1':'v1',
       'k2':'v2',
       'k3':'v3'}


def func(msg,*args,**kwargs):
    print(msg, args, kwargs)
    print('msg',msg)
    print(kwargs)
    for key,value in kwargs.items():
        if key == 'k1':
            print(value,'11111111')

func('abc',**dic)