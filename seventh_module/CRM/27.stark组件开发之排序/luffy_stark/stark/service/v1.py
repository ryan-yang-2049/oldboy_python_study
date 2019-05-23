# -*- coding: utf-8 -*-

import functools
from types import FunctionType
from django.conf.urls import url
from django.shortcuts import HttpResponse, render, redirect
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.http import QueryDict

from stark.utils.pagination import Pagination
from stark.forms.base import StarkModelForm
from stark.utils.parse_url import ParseUrl


def get_choice_text(title, field):
	"""
	对于Stark组件中定义列时，choice如果想要显示中文信息，调用此方法即可。
	:param title: 希望页面显示的表头
	:param field: 字段名称
	:return:
	"""

	def inner(self, obj=None, is_header=None):
		if is_header:
			return title
		method = "get_%s_display" % field
		return getattr(obj, method)()
	return inner


class StarkHandler(object):
	list_display = []  # 页面显示列
	per_page_num = 10  # 每页显示格式
	has_add_btn = True  # 是否具有添加按钮

	def __init__(self, site, model_class, prev):
		self.site = site
		self.model_class = model_class  # 此时的model_class 是一个对象
		self.prev = prev  # 表示别名
		self.request = None  # 主要用于保存访问对象的request信息

	# 编辑按钮
	def display_edit(self, obj=None, is_header=None):
		"""
		自定义页面显示的列（表头和内容）
		:param obj:
		:param is_header:
		:return:
		"""
		if is_header:
			return "编辑"
		parse_url = ParseUrl(request=self.request, namespace=self.site.namespace, name=self.get_change_url_name,
		                     pk=obj.pk)
		url = parse_url.memory_reverse_url()
		return mark_safe('<a href="%s">编辑</a>' % url)

	# 删除按钮
	def display_del(self, obj=None, is_header=None):
		if is_header:
			return "删除"
		parse_url = ParseUrl(request=self.request, namespace=self.site.namespace, name=self.get_delete_url_name,
		                     pk=obj.pk)
		url = parse_url.memory_reverse_url()
		return mark_safe('<a href="%s">删除</a>' % url)

	# 添加按钮的钩子函数
	def get_add_btn(self):
		if self.has_add_btn:
			# 根据别名反向生成URL
			parse_url = ParseUrl(self.request, self.site.namespace, self.get_add_url_name)
			url = parse_url.memory_reverse_url()
			return '<a class="btn btn-primary" href="%s">添加</a>' % (url)
		return None

	model_form_class = None

	def get_model_form_class(self):
		if self.model_form_class:
			return self.model_form_class
		else:
			class DynamicModelForm(StarkModelForm):
				class Meta:
					model = self.model_class
					fields = '__all__'

		return DynamicModelForm

	order_list = []

	def get_order_list(self):
		return self.order_list or ['id',]  # -id 按照id降序

	search_list = []

	def get_search_list(self):
		return self.search_list

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
		################ 模糊搜索 #############
		search_list = self.search_list
		"""
		1.如果search_list 中没有之,则不显示搜索框
		2.获取用户提交的关键字
		3.构造条件
		"""
		search_key_value = request.GET.get('q', None)
		print(search_key_value)
		from django.db.models import Q
		# Q　用于构造复杂的ORM查询条件
		conn = Q()
		conn.connector = 'OR'
		if search_key_value:
			for item in search_list:
				conn.children.append((item,search_key_value))

		################ 1.排序处理 #############
		order_list = self.get_order_list()

		################ 2.处理分页 #############
		# 数据库里面所有的数据
		all_data = self.model_class.objects.filter(conn).order_by(*order_list)
		query_params = request.GET.copy()  # copy方法是默认不能修改request.GET里面的参数的
		query_params._mutable = True  # 这样就可以修改request.GET 里面的参数值了

		pager = Pagination(
			current_page=request.GET.get('page'),  # 获取页面返回的获取的页码
			all_count=all_data.count(),  # 数据库里面所有数据的计算
			base_url=request.path_info,  # 访问的基础URL,例如 http://127.0.0.1/abc?name=ryan&age=18 里面的 http://127.0.0.1
			params=query_params,
			# 用户URL里面的参数,例如 http://127.0.0.1/abc?name=ryan&age=18里面的name=ryan&age=18,它是 QueryDict类型
			per_page_num=self.per_page_num  # 这个是每页显示的个数(扩展，可以在网页端输入，然后在传入服务器端)
		)

		# 列表展示页使用分页的设置 （切片的应用）
		data_list = all_data[pager.start:pager.end]

		################ 3.处理表格 #############
		list_display = self.get_list_display()
		# 3.1 处理表头
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

		# 3.2 处理表的内容
		# queryset[对象1，对象2]
		body_list = []
		for row in data_list:
			tr_list = []
			if list_display:
				for key_or_func in list_display:
					if isinstance(key_or_func, FunctionType):
						tr_list.append(key_or_func(self, row, is_header=False))
					else:
						tr_list.append(getattr(row, key_or_func))
			else:
				tr_list.append(row)
			body_list.append(tr_list)

		################ 4.添加按钮 #############
		add_btn = self.get_add_btn()
		return render(request, 'stark/changelist.html', locals())

	def form_database_save(self, form, is_update=False):  # 视频中的save
		"""
		在使用ModelForm保存数据之前，预留的钩子方法
		:param form:
		:param is_update:
		:return:
		"""
		form.save()

	def add_view(self, request):
		"""
		添加页面
		:param request:
		:return:
		"""
		model_form_class = self.get_model_form_class()
		if request.method == "GET":
			form = model_form_class()
			return render(request, 'stark/change.html', {"form": form})

		form = model_form_class(data=request.POST)
		if form.is_valid():
			self.form_database_save(form, is_update=False)
			# 在数据库中保存成功后,跳转回列表页面（携带原来的参数）
			parse_url = ParseUrl(request=self.request, namespace=self.site.namespace, name=self.get_list_url_name)
			url = parse_url.memory_url()
			return redirect(url)
		return render(request, 'stark/change.html', {"form": form})

	def change_view(self, request, pk):
		"""
		编辑页面
		:param request:
		:return:
		"""
		# 当前编辑对象
		current_change_object = self.model_class.objects.filter(pk=pk).first()
		if not current_change_object:
			return HttpResponse("需要修改的对象不存在，请重新选择")

		model_form_class = self.get_model_form_class()
		if request.method == "GET":
			form = model_form_class(instance=current_change_object)
			return render(request, 'stark/change.html', {"form": form})

		form = model_form_class(data=request.POST, instance=current_change_object)
		if form.is_valid():
			self.form_database_save(form, is_update=False)
			# 在数据库中保存成功后,跳转回列表页面（携带原来的参数）
			parse_url = ParseUrl(request=self.request, namespace=self.site.namespace, name=self.get_list_url_name)
			url = parse_url.memory_url()
			return redirect(url)
		return render(request, 'stark/change.html', {"form": form})

	def delete_view(self, request, pk):
		"""
		删除页面
		:param request:
		:param pk:
		:return:
		"""
		parse_url = ParseUrl(request=self.request, namespace=self.site.namespace, name=self.get_list_url_name)
		cancel = parse_url.memory_url()
		if request.method == "GET":
			return render(request, 'stark/delete.html', locals())
		current_delete_object = self.model_class.objects.filter(pk=pk).delete()
		return redirect(cancel)

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

	def wrapper(self, func):
		@functools.wraps(func)  # 保留原函数的源信息
		def inner(request, *args, **kwargs):
			self.request = request
			return func(request, *args, **kwargs)

		return inner

	def get_urls(self):
		patterns = [
			url(r'^list/$', self.wrapper(self.changelist_view), name=self.get_list_url_name),
			url(r'^add/$', self.wrapper(self.add_view), name=self.get_add_url_name),
			url(r'^change/(?P<pk>\d+)/$', self.wrapper(self.change_view), name=self.get_change_url_name),
			url(r'^del/(?P<pk>\d+)/$', self.wrapper(self.delete_view), name=self.get_delete_url_name),
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

		self._registry.append(
			{'model_class': model_class, 'handler': handler_calss(self, model_class, prev), 'prev': prev})
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
				patterns.append(url(r'%s/%s/%s/' % (app_label, model_name, prev),
				                    (handler.get_urls(), None, None)))  # 第一个None 是namespace,第二个是name
			else:  # url中不带前缀的
				patterns.append(url(r'%s/%s/' % (app_label, model_name), (handler.get_urls(), None, None)))

		return patterns

	@property
	def urls(self):
		return self.get_urls(), self.app_name, self.namespace


site = StarkSite()
