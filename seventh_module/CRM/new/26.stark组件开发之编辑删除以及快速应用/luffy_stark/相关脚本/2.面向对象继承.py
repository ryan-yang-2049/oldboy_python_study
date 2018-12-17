# -*- coding: utf-8 -*-

# __title__ = '1.面向对象相关.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.12.14'


class Base(object):

	def __init__(self,name):
		self.name = name

	def show_detail(self):
		"""
		显示详细信息
		:return:
		"""
		msg = "我叫 %s,来自于SH。"%self.name
		print(msg)

class Foo(Base):
	def show_detail(self):
		"""
		显示详细信息
		:return:
		"""
		msg = "我叫 %s,来自于BJ。"%self.name
		print(msg)



class Bar(Base):
	pass

obj1 = Foo('a1')
obj1.show_detail()

obj2 = Bar('a2')
obj2.show_detail()


