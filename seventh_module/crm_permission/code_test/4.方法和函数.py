# -*- coding: utf-8 -*-

# __title__ = '4.方法和函数.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.09.17'

def func():
	pass

class Foo(object):

	def display(self):
		pass


# print(func)
#
# print(Foo.display)  # 类直接调用，相当于一个函数

obj = Foo()
# print(obj.display)  # 通过对象调用，那么他就直接定义为一个方法

from types import MethodType,FunctionType
def check(arg):
	"""
	判断 arg是函数则打印1 ，arg是方法则打印2
	:param arg:
	:return:
	"""

	if isinstance(arg,MethodType):
		print(2,"我是方法")
	elif isinstance(arg,FunctionType):
		print(1,"我是函数")
	else:
		print("不认识")


check(func)

check(Foo.display)

check(obj.display)
