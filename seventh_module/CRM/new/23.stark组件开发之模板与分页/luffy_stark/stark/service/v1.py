# -*- coding: utf-8 -*-

from types import FunctionType
from django.conf.urls import url
from django.shortcuts import HttpResponse, render

from stark.utils.pagination import Pagination

class StarkHandler(object):
	list_display = []
	per_page_num = 10
	def __init__(self, model_class, prev):
		self.model_class = model_class  # 此时的model_class 是一个对象
		self.prev = prev  # 表示别名

	def get_list_display(self):
		"""
		获取页面上应该显示的列，预留的自定义扩展，例如：以后根据用户角色的不同展示不同的列
		:return:
		"""
		value = []
		value.extend(self.list_display)

		return value

	def changelist_view(self, request):
		"""
		列表页面
		:param request:
		:return:
		"""
		# 1.处理分页
		# 数据库里面所有的数据
		all_data = self.model_class.objects.all()
		query_params = request.GET.copy()   # copy方法是默认不能修改request.GET里面的参数的
		query_params._mutable = True    # 这样就可以修改request.GET 里面的参数值了

		pager = Pagination(
			current_page=request.GET.get('page'),
			all_count = all_data.count(),
			base_url = request.path_info,
			params = query_params,
			per_page_num= self.per_page_num
		)

		# 列表展示页使用分页的设置
		data_list = all_data[pager.start:pager.end]

		# 处理表格
		list_display = self.get_list_display()
		# 1.处理表头
		header_list = []
		if list_display:  # 如果有list_display(展示列) 就循环它
			for key_or_func in list_display:
				if isinstance(key_or_func, FunctionType):
					verbose_name = key_or_func(self, obj=None, is_header=True)
				else:
					verbose_name = self.model_class._meta.get_field(key_or_func).verbose_name
				header_list.append(verbose_name)
		else:  # 如果没有list_display(展示列)，那么表头就是它的表名
			header_list.append(self.model_class._meta.model_name)

		# 2.处理表的内容
		# queryset[对象1，对象2]

		"""
		获取的数据，要根据list_display 来进行构造数据
		[
			['name1','18','123@qq.com'],
			['name2','28','234@qq.com']
		]
		"""
		body_list = []
		for row in data_list:
			tr_list = []
			if list_display:
				for key_or_func in list_display:
					if isinstance(key_or_func, FunctionType):
						tr_list.append(key_or_func(self, obj=row, is_header=False))
					else:
						tr_list.append(getattr(row, key_or_func))
			else:
				tr_list.append(row)
			body_list.append(tr_list)

		return render(request, 'stark/changelist.html', locals())

	def add_view(self, request):
		"""
		添加页面
		:param request:
		:return:
		"""
		return HttpResponse('添加页面')

	def change_view(self, request, pk):
		"""
		编辑页面
		:param request:
		:return:
		"""
		return HttpResponse('编辑页面')

	def delete_view(self, request, pk):
		"""
		删除页面
		:param request:
		:param pk:
		:return:
		"""
		return HttpResponse('删除页面')

	def get_url_name(self, param):
		app_label, model_name = self.model_class._meta.app_label, self.model_class._meta.model_name

		if self.prev:
			return '%s_%s_%s_%s' % (app_label, model_name, self.prev, param)
		return '%s_%s_%s' % (app_label, model_name, param)

	@property
	def get_list_url_name(self):
		"""
		获取列表页面URL的name
		:return:
		"""
		return self.get_url_name('list')

	@property
	def get_add_url_name(self):
		"""
		获取添加页面URL的name
		:return:
		"""
		return self.get_url_name('add')

	@property
	def get_change_url_name(self):
		"""
		获取修改页面URL的name
		:return:
		"""
		return self.get_url_name('change')

	@property
	def get_delete_url_name(self):
		"""
		获取删除页面URL的name
		:return:
		"""
		return self.get_url_name('delete')

	def get_urls(self):
		patterns = [
			url(r'^list/$', self.changelist_view, name=self.get_list_url_name),
			url(r'^add/$', self.add_view, name=self.get_add_url_name),
			url(r'^change/$', self.change_view, name=self.get_change_url_name),
			url(r'^del/$', self.delete_view, name=self.get_delete_url_name),
		]
		patterns.extend(self.extra_urls())
		return patterns

	def extra_urls(self):
		return []


class StarkSite(object):
	def __init__(self):
		self._registry = []
		self.app_name = 'stark'
		self.namespace = 'stark'

	def registry(self, model_class, handler_calss=None, prev=None):
		"""

		:param model_class: 是调用此方法的app中的 models中相关的类  例如：models.UserInfo
		:param handler_calss: 处理请求的视图函数所在的类
		:param prev: 生成 url 的前缀
		:return:
		"""
		if not handler_calss:
			handler_calss = StarkHandler  # StarkHandler 就是上面创建的类

		self._registry.append({'model_class': model_class, 'handler': handler_calss(model_class, prev), 'prev': prev})
		"""
		site._registry = [
			{'prev':None,'model_class': <class 'app01.models.Depart'>, 'handler': DepartHandler(models.Depart,prev)对象中有一个model_class=models.Depart},
			{'prev':private,'model_class': <class 'app01.models.UserInfo'>, 'handler': StarkHandler(models.UserInfo,prev)对象中有一个model_class=models.UserInfo},    
			{'prev':None,'model_class': <class 'app02.models.Host'>, 'handler': StarkHandler(models.Host,prev)对象中有一个model_class=models.Host}
			]
		"""

	def get_urls(self):
		patterns = []
		for item in self._registry:
			model_class = item['model_class']
			handler = item['handler']  # 此时的handler 其实是一个对象；例如：StarkHandler(models.UserInfo) 对象
			prev = item['prev']
			app_label, model_name = model_class._meta.app_label, model_class._meta.model_name
			# app_label 表示项目下某个应用的名称  ：app01
			# model_name 表示应用的表名称(小写) ：depart
			if prev:  # url中带前缀的
				patterns.append(url(r'%s/%s/%s/' % (app_label, model_name, prev), (handler.get_urls(), None, None)))
			else:  # url中不带前缀的
				patterns.append(url(r'%s/%s/' % (app_label, model_name), (handler.get_urls(), None, None)))

		return patterns

	def urls(self):
		return self.get_urls(), self.app_name, self.namespace


site = StarkSite()
