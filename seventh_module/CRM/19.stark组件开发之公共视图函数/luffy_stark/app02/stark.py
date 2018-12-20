# -*- coding: utf-8 -*-

# __title__ = 'stark.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.12.14'
from django.shortcuts import HttpResponse
from stark.service.v1 import site,StarkHandler

from app02 import models


class HostHandler(StarkHandler):
	pass

site.registry(models.Host,HostHandler)



class RoleHandler(StarkHandler):
	pass

site.registry(models.Role,RoleHandler)