# -*- coding: utf-8 -*-

# __title__ = 'stark.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.12.14'
from django.shortcuts import HttpResponse
from django.conf.urls import url
from django.utils.safestring import mark_safe

from stark.service.v1 import site, StarkHandler
from app01 import models


class DepartHandler(StarkHandler):
	list_display = ['id', 'title']


# site.registry(models.Depart, DepartHandler, prev='public01')
site.registry(models.Depart, DepartHandler)


class UserInfoHandler(StarkHandler):

	def display_edit(self, obj=None, is_header=None):
		"""
		自定义页面显示的列(表头和内容)
		:param obj: obj是列的数据对象，例如  obj.name
		:param is_header: 使用的时候判断是否是表头
		:return:
		"""
		if is_header:
			return "操作"
		return mark_safe('<a href="https://www.baidu.com">编辑</a>')

	def display_del(self, obj=None, is_header=None):
		"""
		自定义页面显示的列(表头和内容)
		:param obj: obj是列的数据对象，例如  obj.name
		:param is_header: 使用的时候判断是否是表头
		:return:
		"""
		if is_header:
			return "删除"
		return mark_safe('<a href="https://www.baidu.com">删除</a>')


	# 定制页面的列
	list_display = ['name', 'age', 'email', display_edit,display_del]



	# def get_list_display(self):
	# 	"""
	# 	自定义扩展，例如：根据用户角色的不同展示不同的列
	# 	:return:
	# 	"""
	# 	return ['id', 'name', 'age']


site.registry(models.UserInfo, UserInfoHandler)
