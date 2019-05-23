# -*- coding: utf-8 -*-

# __title__ = '6.getattr方法.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.12.20'



class People(object):
	country='China'

	def __init__(self,name,age):
		self.name=name
		self.age=age

	def talk(self):
		return  '%s is talking' %self.name

obj=People('lucky',18)

print("getattr 对象属性:",getattr(obj,'name'))
print("getattr 对象绑定方法:",getattr(obj,'talk'))
print("getattr 对象绑定方法的值:",getattr(obj,'talk')())




