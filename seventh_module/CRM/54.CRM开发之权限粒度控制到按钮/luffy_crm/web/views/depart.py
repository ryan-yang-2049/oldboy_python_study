# -*- coding: utf-8 -*-

# __title__ = 'depart.py'
# __author__ = 'YangYang'
# __mtime__ = '2019.02.21'

from stark.service.v1 import StarkHandler
from web.views.base import PermissionHandler
class DepartmentHandler(PermissionHandler,StarkHandler):
	list_display = ['title']
