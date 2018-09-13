# -*- coding: utf-8 -*-

# __title__ = '1.类是否可以当做字典的key.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.09.04'



class User(object):
	pass
class Role(object):
	pass
class Bar(object):
	def __init__(self,b):
		self.b = b
_registry = {
	User:Bar(User),
	Role:Bar(Role)
}

for k,v in _registry.items():
	print(k,v.b)

'''
结果：
<class '__main__.User'> <class '__main__.User'>
<class '__main__.Role'> <class '__main__.Role'>
'''



