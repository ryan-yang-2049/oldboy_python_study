# -*- coding: utf-8 -*-
"""
__title__ = '继承.py'
__author__ = 'yangyang'
__mtime__ = '2018.01.22'
"""
class ParentClass1:
    pass

class ParentClass2:
    pass

class SubClass1(ParentClass1):
    pass

class SubClass2(ParentClass1,ParentClass2):
    pass

print(SubClass1.__bases__)   #查看继承的父类
print(SubClass2.__bases__)



print(SubClass2.__mro__)







