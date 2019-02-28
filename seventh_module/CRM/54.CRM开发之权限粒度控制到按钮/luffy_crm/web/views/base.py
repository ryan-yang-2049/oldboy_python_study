# -*- coding: utf-8 -*-
"""
__title__ = 'base.py'
__author__ = 'yangyang'
__mtime__ = '2019-02-28'
"""

class PermissionHandler(object):

	# 控制添加按钮
	# 是否显示添加按钮
	def get_add_btn(self, request, *args, **kwargs):
		from django.conf import settings
		# 当前用户所有的权限信息
		permissions_dict = request.session.get(settings.PERMISSION_SESSION_KEY)
		if self.get_add_url_name not in permissions_dict:
			return None
		return super().get_add_btn(request, *args, **kwargs)

	# 是否显示编辑按钮
	def get_list_display(self,request,*args,**kwargs):
		from django.conf import settings
		# 当前用户所有的权限信息
		permissions_dict = request.session.get(settings.PERMISSION_SESSION_KEY)
		value = []
		if self.list_display:
			value.extend(self.list_display)
			# 如果当前用户有编辑的权限，则设置编辑的按钮
			# 如果当前用户有删除的权限，则设置删除的按钮
			if self.get_change_url_name in  permissions_dict and self.get_delete_url_name in permissions_dict:
				value.append(type(self).display_edit_del)
			elif self.get_change_url_name in  permissions_dict :
				value.append(type(self).display_edit)
			elif self.get_delete_url_name in permissions_dict:
				value.append(type(self).display_del)

		return value









