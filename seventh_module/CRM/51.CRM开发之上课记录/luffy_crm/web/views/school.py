# -*- coding: utf-8 -*-

# __title__ = 'school.py'
# __author__ = 'YangYang'
# __mtime__ = '2019.02.21'


from stark.service.v1 import StarkHandler


class SchoolHandler(StarkHandler):
	list_display = ['title']
