# -*- coding: utf-8 -*-

from django.shortcuts import HttpResponse
from stark.service.v1 import site,StarkHandler

from app01 import models

class DepartHandler(StarkHandler):
	pass

site.registry(models.Depart,DepartHandler)


class UserInfoHandler(StarkHandler):
	pass


site.registry(models.UserInfo,UserInfoHandler)






