# -*- coding: utf-8 -*-

# __title__ = 'v1.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.12.14'
from django.conf.urls import url
from django.shortcuts import HttpResponse

class StarkSite(object):
	def __init__(self):
		self._registry = []
		self.app_name = 'stark'
		self.namespace = 'stark'

	def registry(self, model_class, handler_calss):
		"""

		:param model_class: 是调用此方法的app中的 models中相关的类  例如：models.UserInfo
		:param handler_calss: 处理请求的视图函数所在的类
		:return:
		"""
		self._registry.append({'model_class': model_class, 'handler': handler_calss(model_class)})
		"""
		site._registry = [
			{'model_class': <class 'app01.models.Depart'>, 'handler': <app01.stark.DepartHandler object at 0x000001D67189F358>},
			{'model_class': <class 'app01.models.UserInfo'>, 'handler': <app01.stark.UserInfoHandler object at 0x000001D67189F748>},    
			{'model_class': <class 'app02.models.Host'>, 'handler': <app02.stark.HostHandler object at 0x000001D67189FB38>}
			]
		"""

	def get_urls(self):
		patterns = []
		for item in self._registry:
			model_class = item['model_class']
			handler = item['handler']
			app_label,model_name = model_class._meta.app_label,model_class._meta.model_name
			# app_label 表示项目下某个应用的名称  ：app01
			# model_name 表示应用的表名称(小写) ：depart
			patterns.append(url(r'%s/%s/list/$'%(app_label,model_name), handler.changelist_view))
			patterns.append(url(r'%s/%s/add/$'%(app_label,model_name), handler.add_view))
			patterns.append(url(r'%s/%s/edit/(\d+)/$'%(app_label,model_name), handler.change_view))
			patterns.append(url(r'%s/%s/del/(\d+)/$'%(app_label,model_name), handler.delete_view))

		return patterns

	def urls(self):
		return self.get_urls(), self.app_name, self.namespace


site = StarkSite()
