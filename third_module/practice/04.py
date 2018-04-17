# -*- coding: utf-8 -*-
"""
__title__ = '04.py'
__author__ = 'yangyang'
__mtime__ = '2018.01.26'
"""
class A:
	def __init__(self):
		print("__init__ ")
		print(self)
		super(A, self).__init__()

	def __new__(cls):
		print("__new__ ")
		self = super(A, cls).__new__(cls)
		print(self)
		return self

A()











