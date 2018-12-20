# -*- coding: utf-8 -*-

# __title__ = 'stark.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.12.14'
from django.shortcuts import HttpResponse
from django.conf.urls import url
from stark.service.v1 import site, StarkHandler

from app01 import models


class DepartHandler(StarkHandler):

	# 预留的钩子函数，用于单独的对象添加额外的URL
	def extra_urls(self):
		"""
		额外的增加URL
		:return:
		"""
		extar_patterns = [
			url(r'^detail/(\d+)/$', self.detail_view,name='detail'),
		]

		return extar_patterns

	def detail_view(self, request, pk):
		return HttpResponse("详情页面")


site.registry(models.Depart, DepartHandler,prev='public01')


class UserInfoHandler(StarkHandler):

	# 对于某个对象需要减少几个URL,那就单独写这个函数并加上需要的URL即可
	def get_urls(self):
		"""
		修改父类 StarkHandler 默认的URL
		:return:
		"""
		patterns = [
			url(r'^list/$', self.changelist_view,name=self.get_add_url_name),
			url(r'^add/$', self.add_view,name=self.get_add_url_name),
		]

		return patterns


site.registry(models.UserInfo, UserInfoHandler,prev='public02')


