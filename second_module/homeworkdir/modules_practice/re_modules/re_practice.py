# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'yangyang'
__mtime__ = '2017.12.22'
"""
import io
import re

pattern = re.compile('(1[3458]\d{9})')
with  io.open("test",'r',encoding="utf-8") as f:
    for line in f.readlines():
        res = re.findall(pattern,line)
        if res:
            print(res)




pattern = re.compile('(\w+@\w+.(cn|com))')
with io.open("email_info",'r',encoding="utf-8") as f:
    for line in f.readlines():
        # print(line)
        res = re.findall(pattern,line)

        if res:
            print(res)


