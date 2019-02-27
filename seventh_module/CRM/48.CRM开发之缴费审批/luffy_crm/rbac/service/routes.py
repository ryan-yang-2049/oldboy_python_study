# -*- coding: utf-8 -*-

# __title__ = 'routes.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.12.06'

import re
from collections import OrderedDict
from django.shortcuts import HttpResponse,render,redirect
from django.conf import settings
from django.utils.module_loading import import_string # 根据字符串导入一个模块
from django.urls import RegexURLPattern,RegexURLResolver


def check_url_exclude(url):
	"""
	排除一些特定的URL
	:param url:
	:return:
	"""
	exclude_url = settings.AUTO_DISCOVER_EXCLUDE

	for regex in exclude_url:
		if re.match(regex,url):
			return True

def recursion_urls(pre_namespace,pre_url,urlpatterns,url_ordered_dict):
	"""
	递归的获取URL
	:param pre_namespace: namespace前缀，以后用于拼接name
	:param pre_url: url前缀，以后用于拼接url
	:param urlpatterns: 路由关系列表
	:param url_ordered_dict: 用于保存递归中获取的所有路由
	:return:
	"""
	for item in urlpatterns:
		if isinstance(item,RegexURLPattern):    # 非路由分发，将路由添加到url_ordered_dict 中
			if not item.name:
				continue

			if pre_namespace:
				name = "%s:%s"%(pre_namespace,item.name)
			else:
				name = item.name
			url = pre_url + item._regex # /^rbac/^user/reset/password/(?P<pk>\d+)/$
			url = url.replace('^','').replace('$','') # /rbac/user/reset/password/(?P<pk>\d+)/

			if check_url_exclude(url):  # 排除url
				continue

			url_ordered_dict[name] = {'name':name,"url":url}

		elif isinstance(item,RegexURLResolver): # 路由分发，继续递归处理
			if pre_namespace:       # 视频 42 自动发现项目中的所有URL
				if item.namespace:
					namespace = "%s:%s"%(pre_namespace,item.namespace)
				else:
					namespace = item.namespace
			else:
				if item.namespace:
					namespace = item.namespace
				else:
					namespace = None
			recursion_urls(namespace, pre_url+item.regex.pattern, item.url_patterns, url_ordered_dict)


def get_all_url_dict():
	"""
	获取项目中所有的URL（url中必须有name别名）
	:return:
	"""

	url_ordered_dict = OrderedDict()
	md = import_string(settings.ROOT_URLCONF)   # 相当于  from luffy_permission import urls
	# for item in md.urlpatterns:
	recursion_urls(None,'/',md.urlpatterns,url_ordered_dict)    # 递归的获取所有的路由
	return url_ordered_dict












