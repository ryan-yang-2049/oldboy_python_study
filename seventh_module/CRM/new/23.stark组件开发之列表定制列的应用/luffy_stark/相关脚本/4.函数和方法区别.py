# -*- coding: utf-8 -*-
"""
__title__ = '4.函数和方法区别.py'
__author__ = 'yangyang'
__mtime__ = '2018-12-15'
"""

class Foo(object):

	def func(self,name):
		print(name)

obj = Foo()
# obj.func('ryan') # 方法
print(obj.func) # <bound method Foo.func of <__main__.Foo object at 0x105f7c5f8>>

# obj = Foo()
# Foo.func(obj,'ryan') # 函数
print(Foo.func) # <function Foo.func at 0x1060cb6a8>



