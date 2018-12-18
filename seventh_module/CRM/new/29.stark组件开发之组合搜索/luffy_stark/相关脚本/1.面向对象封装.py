# -*- coding: utf-8 -*-

# __title__ = '1.面向对象相关.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.12.14'


class Foo(object):

	def __init__(self,name):
		self.name = name

	def show_detail(self):
		"""
		显示详细信息
		:return:
		"""
		msg = "我叫 %s,来自于SH。"%self.name
		print(msg)


obj1 = Foo('a1')
obj2 = Foo('a2')
obj3 = Foo('a3')

obj1.show_detail()
obj2.show_detail()
obj3.show_detail()




