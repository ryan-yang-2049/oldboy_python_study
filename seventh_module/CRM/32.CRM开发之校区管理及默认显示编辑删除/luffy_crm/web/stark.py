# -*- coding: utf-8 -*-

# __title__ = 'stark.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.12.24'

from stark.service.v1 import site, StarkHandler
from web import models


class SchoolHandler(StarkHandler):
	list_display = ['title']
	order_list = ['-title']

site.registry(models.School, SchoolHandler)



class DepartmentHandler(StarkHandler):
	list_display = ['title']


site.registry(models.Department,DepartmentHandler)

















