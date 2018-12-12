# -*- coding: utf-8 -*-
"""
__title__ = 'rbac.py'
__author__ = 'ryan'
__mtime__ = '2018/10/11'
"""

import re
from django.http import QueryDict
from collections import OrderedDict
from  django.template import Library
from django.urls import reverse
from django.conf import settings

from rbac.service import parse_urls
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
	print("ordered_dict",ordered_dict)
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
	判断是否有权限,按钮菜单
	:param request:
	:param name:
	:return:
	"""
	if name in request.session[settings.PERMISSION_SESSION_KEY]:
		return True



@register.simple_tag
def memory_url(request,name,*args,**kwargs):
	"""
	生成带有原搜索条件的URL(替换模板中的 {% url %})
	:param request: 获取path_info 后面的值
	:param name:    反向解析url
	:param args:    传递的pk值
	:param kwargs:  传递的pk=row.id 值
	:return:
	"""
	return parse_urls.memory_url(request,name,*args,**kwargs)




