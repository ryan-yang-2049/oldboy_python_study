# -*- coding: utf-8 -*-

# __title__ = '继承关系.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.09.14'

"""
class StarkConfig(object):
	def __init__(self,model_class,site):
		self.model_class = model_class
		self.site = site

	def func(self):
		print(666)

class RoleConfig(StarkConfig):

	def func(self):
		print(999)

obj1 = StarkConfig(11,22)
obj1.func()

obj2 = RoleConfig(33,44)
obj2.func()

# 示例2：
class StarkConfig(object):
	def __init__(self,model_class,site):
		self.model_class = model_class
		self.site = site

	def func(self):
		print(666)

	def run(self):
		self.func()

class RoleConfig(StarkConfig):

	def func(self):
		print(999)

obj1 = StarkConfig(11,22)
obj1.run()  # 666

obj2 = RoleConfig(33,44)
obj2.run()   # 999
"""
class StarkConfig(object):
	def __init__(self,model_class,site):
		self.model_class = model_class
		self.site = site

	def func(self):
		print(self.site)

	def run(self):
		self.func()

class RoleConfig(StarkConfig):

	def func(self):
		print(self.site)

obj1 = StarkConfig(11,22)
obj1.run()  # 22

obj2 = RoleConfig(33,44)
obj2.run()  # 55


