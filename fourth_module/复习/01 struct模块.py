# -*- coding: utf-8 -*-
"""
__title__ = '01 struct模块.py'
__author__ = 'yangyang'
__mtime__ = '2018.03.07'
"""
import  struct

# struct 模块可以把一个类型，如数字，转成固定长度的bytes类型。
# 在一定大小范围类的数字（也就是下面的 1234510） 经过pack以后，长度都为 4
res = struct.pack('i',1234510)
print(res,len(res),type(res))

unpack_res = struct.unpack('i',res)
print(unpack_res[0])






