# -*- coding: utf-8 -*-
"""
__title__ = 'rbac.py'
__author__ = 'ryan'
__mtime__ = '2018/10/11'
"""

import re
from collections import OrderedDict
from  django.template import Library

from django.conf import settings

register = Library()

@register.inclusion_tag('rbac/static_menu.html')
def  static_menu(request):
	"""
	创建一级菜单
	:return:
	"""

	menu_list = request.session.get(settings.MENU_SESSION_KEY)
	return {'menu_list':menu_list}

@register.inclusion_tag('rbac/mutli_menu.html')
def  mutli_menu(request):
	"""
	创建二级菜单
	:return:
	"""
	'''
		menu_dict =	{
						1:{
							title:'信息管理',
							icon : 'x1',
							children:[
								{'title':'客户列表','url':'/customer/list/'},
								{'title':'账单列表','url':'/account/list'},
							]
						},
						2:{
							title:'客户信息',
							icon : 'x1',
							children:[
								{'title':'个人资料','url':'/userinfo/list/'},
							]
						},
					}

	'''

	menu_dict = request.session.get(settings.MENU_SESSION_KEY)  # 此处获取的值是从初始化权限py中得到的 --> init_permission.py
	# print(request.current_selected_permission,type(request.current_selected_permission))
	# print("url_record=========>",request.breadcrumb)
	# 对字典的key进行排序。因为字典无序，所以排序的意义在于生成的列表顺序一样。
	key_list = sorted(menu_dict)

	# 创建一个空的有序字典
	ordered_dict = OrderedDict()
	for key in key_list:
		val = menu_dict[key]
		val['class'] = 'hide'
		for per in val['children']:
			if per['id'] == request.current_selected_permission:
				per['class'] = 'active'
				val['class'] = ''
		ordered_dict[key] = val

	return {'menu_dict':ordered_dict}

# 导航条
@register.inclusion_tag('rbac/breadcrumb.html')
def breadcrumb(request):
	"""
	导航条
	:param request:
	:return: 返回当行的列表
	"""
	return {'record_list':request.breadcrumb}

@register.filter
def has_permission(request,name):
	"""
	判断是否有权限
	:param request:
	:param name:
	:return:
	"""
	if name in request.session[settings.PERMISSION_SESSION_KEY]:
		return True










