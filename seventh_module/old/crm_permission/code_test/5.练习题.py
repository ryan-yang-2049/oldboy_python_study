# -*- coding: utf-8 -*-

# __title__ = '5.练习题.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.09.17'


class RoleConfig(object):

	def f1(self,arg):
		print('f1',arg)

	def f2(self,arg):
		print('f2',arg)


	def f3(self,arg):
		print('f3',arg)

	list_display = [f1,f2]

	def get_list_display(self):
		v = []
		v.extend(self.list_display)
		v.insert(0,RoleConfig.f3)
		return v


obj1 = RoleConfig()
for item in obj1.get_list_display():
	item(obj1,2)

obj2 = RoleConfig()
for item in obj2.get_list_display():
	item(obj2,6)
