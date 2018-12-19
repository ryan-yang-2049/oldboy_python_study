# -*- coding: utf-8 -*-

# __title__ = '5.可迭代对象.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.12.19'

"""
如果一个类中定义了 __iter__ 方法且该方法返回一个迭代器，那么就称该类实例化的对象为一个可迭代对象（对象可以被循环）

迭代器和生成器，生成器是一种特殊的迭代器

"""


class SearchGroupRow(object):
	def __init__(self, queryset_or_tuple):
		"""

		:param queryset_or_tuple: 组合搜索关联获取到的数据
		"""
		self.queryset_or_tuple = queryset_or_tuple

	def __iter__(self):
		return iter(self.queryset_or_tuple)

row = SearchGroupRow([11,22,33])

for item in row:
	print(item)




