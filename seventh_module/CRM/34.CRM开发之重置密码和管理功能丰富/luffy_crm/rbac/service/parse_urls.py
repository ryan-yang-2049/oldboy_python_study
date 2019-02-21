# -*- coding: utf-8 -*-

# __title__ = 'parse_urls.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.12.04'

from django.urls import reverse
from django.http import QueryDict


def memory_url(request, name, *args, **kwargs):
	"""
	生成带有原搜索条件的URL(替换模板中的 {% url %})
	:param request: 获取path_info 后面的值
	:param name:    反向解析url
	:param args:    传递的pk值
	:param kwargs:  传递的pk=row.id 值
	:return:
	"""
	basic_url = reverse(name, args=args, kwargs=kwargs)
	# 当前url中无参数
	if not request.GET:
		return basic_url

	query_dict = QueryDict(mutable=True)

	query_dict['_filter'] = request.GET.urlencode()

	return "%s?%s" % (basic_url, query_dict.urlencode())


def memory_reverse_url(request, name, *args, **kwargs):
	"""
	搭配 templatetags 中的memory_url使用
	反向生成URL
		http://127.0.0.1:8000/rbac/menu/edit/2/?_filter=mid%3D2
		1.在url中将原来的搜索条件,如filter后面的值
		2.reverse 生成原来的url 如：/rbac/menu/list/
		3.拼接之前的url ：/rbac/menu/list/?_filter=mid%3D2

	:param request:
	:param name:
	:param args:
	:param kwargs:
	:return:
	"""
	url = reverse(name, args=args, kwargs=kwargs)
	origin_params = request.GET.get('_filter')
	if origin_params:
		url = "%s?%s" % (url, origin_params)

	return url
