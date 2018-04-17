# -*- coding: utf-8 -*-
"""
__title__ = 'ex03.py'
__author__ = 'yangyang'
__mtime__ = '2018.01.26'
"""


class A:
	def __test(self):
		print("A.test")

	def func(self):
		print("A.func")
		self.__test()


class B(A):
	def __test(self):
		print("B.test")


b = B()
b.func()









