# -*- coding: utf-8 -*-

# __title__ = '类是否可以当做字典的key.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.09.14'

class User(object):
	pass

class Role(object):
	pass

class Bar(object):
	def __init__(self,b):
		self.b = b

_registry = {
	User:Bar(User),       # 对象之间存在嵌套关系
	Role:Bar(Role),

}


for k,v in _registry.items():
	print(k,v.b)






