# -*- coding: utf-8 -*-

# __title__ = 'parse_url.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.12.17'



from django.urls import reverse
from django.http import QueryDict

class ParseUrl(object):
	"""
	保留原搜索条件
	"""
	def __init__(self,request,namespace,name,*args,**kwargs):
		self.request = request
		self.namespace= namespace
		self.name = name
		self.args = args
		self.kwargs = kwargs
		self.nameinfo = "%s:%s"%(self.namespace,self.name)

	def memory_reverse_url(self):
		"""
		保留搜索的url参数到新的页面
		:return:
		"""
		base_url = reverse(self.nameinfo,args=self.args,kwargs=self.kwargs)
		if not  self.request.GET:
			url = base_url
		else:
			param = self.request.GET.urlencode()
			new_query_dict = QueryDict(mutable=True)
			new_query_dict['_filter'] = param
			url = "%s?%s"%(base_url,new_query_dict.urlencode())

		return url

	def memory_url(self):
		"""
		页面提交以后返回原始搜索页面
		:return:
		"""
		base_url = reverse(self.nameinfo, args=self.args, kwargs=self.kwargs)
		params = self.request.GET.get("_filter")
		if not params:
			return base_url
		url = "%s?%s"%(base_url,params)
		return url












