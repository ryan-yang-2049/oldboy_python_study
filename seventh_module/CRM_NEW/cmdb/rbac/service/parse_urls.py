# -*- coding: utf-8 -*-

from django.urls import reverse
from django.http import QueryDict

def  memory_url(request,name,*args,**kwargs):
	"""
	生成带有原搜索条件的URL(替换模板中的 {% url %})
	:param request: 获取path_info 后面的值
	:param name:    反向解析url
	:param args:    传递的pk值
	:param kwargs:  传递的pk=row.id 值
	:return:
	"""
	basic_url = reverse(name,args=args,kwargs=kwargs)

	if not request.GET:return basic_url
	query_dict = QueryDict(mutable=True)
	query_dict['_filter'] = request.GET.urlencode()

	return "%s?%s"%(basic_url,query_dict.urlencode())


def memory_reverse(request, name, *args, **kwargs):
	"""
	反向生成URL
		1.在url中生成原来的搜索条件
	:param request:
	:param name:
	:return:
	"""
	url = reverse(name, args=args, kwargs=kwargs)
	origin_params = request.GET.get('_filter')
	if origin_params:
		url = "%s?%s" % (url, origin_params)
	return url
