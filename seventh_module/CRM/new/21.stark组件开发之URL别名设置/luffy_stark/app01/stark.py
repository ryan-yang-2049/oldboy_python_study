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
			url(r'^detail/(\d+)/$', self.detail_view),
		]
		"""
		除了默认的URL,还新增了一个URL
				^stark/ app01/depart/ ^list/$
				^stark/ app01/depart/ ^add/$
				^stark/ app01/depart/ ^change/$
				^stark/ app01/depart/ ^del/$
				^stark/ app01/depart/ ^detail/(\d+)/$
		"""
		return extar_patterns

	def detail_view(self, request, pk):
		return HttpResponse("详情页面")


site.registry(models.Depart, DepartHandler)


class UserInfoHandler(StarkHandler):

	# 对于某个对象需要减少几个URL,那就单独写这个函数并加上需要的URL即可
	def get_urls(self):
		"""
		修改父类 StarkHandler 默认的URL
		:return:
		"""
		patterns = [
			url(r'^list/$', self.changelist_view),
			url(r'^add/$', self.add_view),
		]
		"""
		就剩下两个URL：
			^stark/ app01/userinfo/ ^list/$
			^stark/ app01/userinfo/ ^add/$
		"""
		return patterns


site.registry(models.UserInfo, UserInfoHandler)

"""
URL加前缀
site.registry(models.UserInfo,prev='private')
site.registry(models.UserInfo,prev='public')
这样就会生成8个带前缀的url
	^stark/ app01/userinfo/private/list/$
	^stark/ app01/userinfo/private/add/$
	^stark/ app01/userinfo/private/change/(\d+)/$
	^stark/ app01/userinfo/private/del/(\d+)/$
	
	^stark/ app01/userinfo/public/list/$
	^stark/ app01/userinfo/public/add/$
	^stark/ app01/userinfo/public/change/(\d+)/$
	^stark/ app01/userinfo/public/del/(\d+)/$


site.registry(models.UserInfo)
如果不写，就只有4个URL
	^stark/ app01/userinfo/list/$
	^stark/ app01/userinfo/add/$
	^stark/ app01/userinfo/change/(\d+)/$
	^stark/ app01/userinfo/del/(\d+)/$
"""
