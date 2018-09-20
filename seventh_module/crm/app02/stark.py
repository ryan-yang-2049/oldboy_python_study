# -*- coding: utf-8 -*-

# __title__ = 'stark.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.09.04'


from stark.service.stark import site,StarkConfig
from app02 import models
from django.conf.urls import url
from django.shortcuts import HttpResponse

class RoleConfig(StarkConfig):
	order_by = ['id']
	list_display = [StarkConfig.display_checkbox,'id','title',StarkConfig.display_edit_del]

	# def get_list_display(self):
	# 	#此为钩子函数，自定制list_display
	# 	# 例如:根据用户角色的不同，显示不同的列
	#
	# 	if 1==1:
	# 		return ['id','title']
	# 	else:
	# 		return ['id']
	#
	# 	# return self.list_display


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





