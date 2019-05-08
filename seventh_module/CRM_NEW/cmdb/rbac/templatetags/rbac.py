# -*- coding: utf-8 -*-

import re
from collections import OrderedDict
from django.template import Library
from django.conf import settings
from django.http import QueryDict
from  django.urls import reverse

from  rbac.service import parse_urls

register = Library()

@register.inclusion_tag('rbac/static_menu.html')
def static_menu(request):
	"""
	创建一级菜单
	:return:
	"""
	menu_list = request.session.get(settings.MENU_SESSION_KEY)
	return {'menu_list': menu_list}


@register.inclusion_tag('rbac/multi_menu.html')
def multi_menu(request):
	"""
	创建二级菜单
	:return:
	"""
	menu_dict = request.session.get(settings.MENU_SESSION_KEY)
	key_list = sorted(menu_dict)
	ordered_dict = OrderedDict()
	for key in key_list:
		val = menu_dict[key]
		val['class'] = 'hide'
		val['display'] = 'none'
		for per in val['children']:

			if per['id'] == request.current_selected_permission:  # 第19课
				per['class'] = 'active'
				val['class'] = ''
				val['display'] = 'block'
		ordered_dict[key] = val
	return {'menu_dict': ordered_dict}


@register.inclusion_tag('rbac/breadcrumb.html')
def breadcrumb(request):

	breadcrumb_info = request.breadcrumb

	return {'breadcrumb_info':breadcrumb_info}

@register.filter
def has_permission(request,name):
	"""
	判断是否有权限，此方法，最多只有两个参数
	在 template html 中的用法为  {% if request|has_permission:"name" %}
	第一个参数放在 | 前面，第二个参数放在 ":" 后面(字符串)
	:param request:
	:param name:
	:return:
	"""
	if name in request.session.get(settings.PERMISSION_SESSION_KEY):
		return True


@register.simple_tag()
def  memory_url(request,name,*args,**kwargs):
	"""
	生成带有原搜索条件的URL(替代模板中的url)
	:param request:
	:param name:
	:return:
	"""
	return parse_urls.memory_url(request,name,*args,**kwargs)








