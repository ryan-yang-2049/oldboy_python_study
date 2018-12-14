# -*- coding: utf-8 -*-

# __title__ = 'stark.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.12.14'
from django.shortcuts import HttpResponse
from django.conf.urls import url
from stark.service.v1 import site, StarkHandler

from app01 import models


class DepartHandler(StarkHandler):
	list_display = ['id', 'title']


# site.registry(models.Depart, DepartHandler, prev='public01')
site.registry(models.Depart, DepartHandler)


class UserInfoHandler(StarkHandler):
	# 定制页面的列
	list_display = ['name', 'age', 'email']


	def get_list_display(self):
		"""
		自定义扩展，例如：根据用户角色的不同展示不同的列
		:return:
		"""
		return ['id','name','age']


site.registry(models.UserInfo, UserInfoHandler)
