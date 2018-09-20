# -*- coding: utf-8 -*-

# __title__ = '1.继承关系.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.09.17'



class StarkConfig(object):
	list_display = []

	def __init__(self,model_class):
		self.model_class = model_class


	def changelist_view(self,request):
		print(self.list_display)
		return 123


class RoleConfig(StarkConfig):
	list_display = ['id','name']
	# def changelist_view(self,request):
	# 	return 666




obj1 = StarkConfig('1')
obj2 = RoleConfig('2')

obj1.changelist_view(1) # []
obj2.changelist_view(2) # ['id', 'name']

