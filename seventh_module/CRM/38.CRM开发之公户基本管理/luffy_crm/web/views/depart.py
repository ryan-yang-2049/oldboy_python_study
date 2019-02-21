# -*- coding: utf-8 -*-

# __title__ = 'depart.py'
# __author__ = 'YangYang'
# __mtime__ = '2019.02.21'

from stark.service.v1 import StarkHandler

class DepartmentHandler(StarkHandler):
	list_display = ['title']
