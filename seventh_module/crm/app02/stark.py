# -*- coding: utf-8 -*-

# __title__ = 'stark.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.09.04'


from stark.service.stark import site,StarkConfig
from app02 import models
from django.conf.urls import url
from django.shortcuts import HttpResponse

class RoleConfig(StarkConfig):

	def func(self):
		print("RoleConfig",self.model_class)


	def extra_url(self):
		data = [
			url(r'^xxx/',self.xxx)
		]
		return data
	def xxx(self,request):
		print('...')
		return HttpResponse('xxxx')

site.register(models.Role,RoleConfig)





