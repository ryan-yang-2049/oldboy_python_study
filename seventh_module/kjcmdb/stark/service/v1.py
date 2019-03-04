# -*- coding: utf-8 -*-

import functools
from types import FunctionType
from django.conf.urls import url
from django.shortcuts import HttpResponse, render, redirect
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.http import QueryDict

from stark.utils.pagination import Pagination
from stark.forms.base import StarkModelForm

from django.db.models import ForeignKey, ManyToManyField


def get_choice_text(title, field):
	"""
	对于Stark组件中定义列时，choice如果想要显示中文信息，调用此方法即可。
	:param title: 希望页面显示的表头
	:param field: 字段名称
	:return:
	"""

	def inner(self, obj=None, is_header=None, *args, **kwargs):
		if is_header:
			return title
		method = "get_%s_display" % field  # obj.get_字段名_display 可以获取choice的值
		return getattr(obj, method)()

	return inner


def get_datetime_text(title, field, time_format='%Y-%m-%d'):
	"""
	定制时间格式化
	:param title: 希望页面显示的表头
	:param field: 字段名称
	:param time_format: 日期要格式化时间格式
	:return:
	"""

	def inner(self, obj=None, is_header=None, *args, **kwargs):
		if is_header:
			return title
		datetime_value = getattr(obj, field)
		return datetime_value.strftime(time_format)

	return inner


def get_m2m_text(title, field):
	"""
	显示manytomany 文本信息
	:param title: 希望页面显示的表头
	:param field: 字段名称
	:param time_format: 日期要格式化时间格式
	:return:
	"""

	def inner(self, obj=None, is_header=None, *args, **kwargs):
		if is_header:
			return title
		queryset_value = getattr(obj, field).all()
		text_list = [str(row) for row in queryset_value]

		return ','.join(text_list)

	return inner


class SearchGroupRow(object):
	def __init__(self, title, queryset_or_tuple, option, query_dict):
		"""

		:param title: 组合搜索的列名称
		:param queryset_or_tuple: 组合搜索关联获取到的数据
		:param option: 调用此方法实例后自己的对象
		:param query_dict: request.GET 的值
		"""
		self.queryset_or_tuple = queryset_or_tuple
		self.title = title
		self.option = option
		self.query_dict = query_dict

	def __iter__(self):
		yield '<div class="whole">%s</div>' % self.title
		yield '<div class="others">'

		total_query_dict = self.query_dict.copy()
		total_query_dict._mutable = True
		origin_value_list = self.query_dict.getlist(self.option.field)  # reuqest.GET 的参数列表
		if not origin_value_list:
			yield "<a class='active' href='?%s'>全部</a>" % total_query_dict.urlencode()
		else:
			total_query_dict.pop(self.option.field)
			yield "<a href='?%s'>全部</a>" % total_query_dict.urlencode()

		for item in self.queryset_or_tuple:
			text = self.option.get_text(item)  # 下面 Option类的 get_text方法
			# 获取组合搜索按钮文本背后的值
			value = str(self.option.get_value(item))  # 数据库里面获取的值 int类型。

			# 获取reuqest.GET ==> QueryDict对象={gender:['1',],depart:['2',]}
			query_dict = self.query_dict.copy()  # 拷贝以后以后，修改自己的，不影响 reuqest.GET 原来的值
			query_dict._mutable = True  # reuqest.GET 默认不能修改，这样设置了才可以被修改

			# origin_value_list = query_dict.getlist(self.option.field)

			if not self.option.is_multi:
				query_dict[self.option.field] = value
				if value in origin_value_list:
					query_dict.pop(self.option.field)
					yield "<a class='active' href='?%s'>%s</a>" % (query_dict.urlencode(), text)
				else:
					yield "<a href='?%s'>%s</a>" % (query_dict.urlencode(), text)
			else:
				# {}
				multi_value_list = query_dict.getlist(self.option.field)
				if value in multi_value_list:
					multi_value_list.remove(value)
					query_dict.setlist(self.option.field, multi_value_list)
					yield "<a class='active' href='?%s'>%s</a>" % (query_dict.urlencode(), text)
				else:
					multi_value_list.append(value)
					query_dict.setlist(self.option.field, multi_value_list)
					yield "<a href='?%s'>%s</a>" % (query_dict.urlencode(), text)
		yield '</div>'


class Option(object):
	def __init__(self, field, is_multi=False, db_condition=None, text_func=None, value_func=None):
		"""

		:param field: 组合搜索的字段
		:param is_multi: 是否支持多选
		:param db_condition: 数据库关联查询时的条件
		:param text_func: 此函数用于显示组合搜索按钮页面文本
		:param value_func: 此函数用于显示组合搜索按钮值
		"""
		self.field = field
		self.is_multi = is_multi
		if not db_condition:
			db_condition = {}
		self.db_condition = db_condition
		self.text_func = text_func

		self.is_choice = False
		self.value_func = value_func

	def get_db_condition(self, request, *args, **kwargs):
		return self.db_condition

	def get_queryset_or_tuple(self, model_class, request, *args, **kwargs):
		"""
		根据字段去获取数据库关联的数据
		:return:
		"""
		# 根据gender或depart字符串，去自己对应的Model类中找到字段对象，
		field_object = model_class._meta.get_field(self.field)
		verbose_name = field_object.verbose_name

		# 根据对象获取关联数据
		if isinstance(field_object, ForeignKey) or isinstance(field_object, ManyToManyField):
			# FK和M2M，应该获取其关联表中的数据
			# 根据表字段获取其关联表的所有数据 field_object.rel.model.objects.all()
			db_condition = self.get_db_condition(request, *args, **kwargs)

			return SearchGroupRow(verbose_name, field_object.rel.model.objects.filter(**db_condition), self,
			                      request.GET)  # 返回的queryset类型,self 是自身的Option对象

		else:
			# 获取Choice中的数据
			self.is_choice = True
			return SearchGroupRow(verbose_name, field_object.choices, self, request.GET)  # 返回的元组类型,self 是自身的Option对象

	def get_text(self, field_object):
		if self.text_func:  # 此为扩展此函数的条件，只要为此类实例化时，可以传递一个自定义的text_func 的函数对象
			return self.text_func(field_object)

		if self.is_choice:
			return field_object[1]

		return str(field_object)

	def get_value(self, field_object):
		if self.value_func:
			return self.value_func(field_object)

		if self.is_choice:
			return field_object[0]

		return field_object.pk


class StarkHandler(object):
	list_display = []  # 页面显示列
	per_page_num = 10  # 每页显示格式
	has_add_btn = True  # 是否具有添加按钮
	delete_template = None
	change_list_template = None

	add_template = None
	change_template = None

	def __init__(self, site, model_class, prev):
		"""

		:param site: 调用此函数的对象自己
		:param model_class: 类似于 models.UserInfo
		:param prev:    URL的前缀，也可以是后缀
		"""
		self.site = site
		self.model_class = model_class  # 此时的model_class 是一个对象
		self.prev = prev  # 表示别名
		self.request = None  # 主要用于保存访问对象的request信息

	def action_multi_delete(self, request, *args, **kwargs):
		"""
		批量删除(如果想要定制成功后的返回值，那么就为action函数设置返回值即可)
		例如：该函数后面加上   return rediret('https://www.baidu.com')
		:param request:
		:return:
		"""
		pk_list = request.POST.getlist('pk')
		self.model_class.objects.filter(id__in=pk_list).delete()

	action_multi_delete.text = '批量删除'

	def action_depart_multi_init(self, request, *args, **kwargs):
		"""
		批量初始化
		:param request:
		:return:
		"""
		pk_list = request.POST.getlist('pk')
		print(pk_list, type(pk_list))
		self.model_class.objects.filter(id__in=pk_list).update(depart_id=3)

	action_depart_multi_init.text = '部门初始化'

	# 组合搜索
	search_group = []

	def get_search_group(self):
		return self.search_group

	def get_search_group_condition(self, request):
		"""
		获取组合搜索的条件
		:param request:
		:return:
		"""
		condition = {}
		# ?depart=1&gender=2&page=123&q=999
		for option in self.get_search_group():
			if option.is_multi:  # 支持多选的时候
				values_list = request.GET.getlist(option.field)  # tags=[1,2]
				if not values_list:
					continue
				condition['%s__in' % option.field] = values_list
			else:  # 不支持多选的时候
				value = request.GET.get(option.field)
				if not value:
					continue
				condition[option.field] = value
		return condition

	def display_checkbox(self, obj=None, is_header=None, *args, **kwargs):
		"""
		自定义页面显示CheckBox
		:param obj:
		:param is_header:
		:return:
		"""
		if is_header:
			return "选择"
		return mark_safe('<input type="checkbox" name="pk" value="%s"/>' % (obj.pk))

	# 编辑
	def display_edit(self, obj=None, is_header=None, *args, **kwargs):
		"""
		自定义页面显示的列（表头和内容）
		:param obj:
		:param is_header:
		:return:
		"""
		if is_header:
			return "编辑"

		return mark_safe('<a href="%s" class="btn btn-success btn-xs">编辑</a>' % self.reverse_change_url(pk=obj.pk))

	# 删除按钮
	def display_del(self, obj=None, is_header=None, *args, **kwargs):
		if is_header:
			return "删除"

		return mark_safe('<a href="%s" class="btn btn-danger btn-xs">删除</a>' % self.reverse_delete_url(pk=obj.pk))

	def display_edit_del(self, obj=None, is_header=None, *args, **kwargs):
		if is_header:
			return "操作"

		tpl = '<a href="%s" class="btn btn-success btn-xs">编辑</a> <a href="%s" class="btn btn-danger btn-xs">删除</a>' % (
			self.reverse_change_url(pk=obj.pk), self.reverse_delete_url(pk=obj.pk))
		return mark_safe(tpl)

	# 添加按钮的钩子函数
	def get_add_btn(self, request, *args, **kwargs):
		if self.has_add_btn:
			# 根据别名反向生成URL

			return '<a class="btn btn-primary" href="%s">添加</a>' % self.reverse_add_url(*args, **kwargs)
		return None

	def get_import_excel_btn(self, request, *args, **kwargs):
		return None

	model_form_class = None

	def get_model_form_class(self, is_add, request, pk, *args, **kwargs):
		"""
		定制添加和编辑页面的ModelForm的定制
		:param is_add:
		:return:
		"""
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
		return self.order_list or ['id']  # -id 按照id降序

	search_list = []

	# 模糊搜索
	def get_search_list(self):
		return self.search_list

	action_list = []

	# 批量执行的下拉狂
	def get_action_list(self):
		return self.action_list

	def get_list_display(self, request, *args, **kwargs):
		"""
		获取页面上应该显示的列，预留的自定义扩展，例如：以后根据用户角色的不同展示不同的列
		:return:
		"""
		value = []
		if self.list_display:
			value.extend(self.list_display)
			value.append(type(self).display_edit_del)

		return value

	def get_queryset(self, request, *args, **kwargs):
		"""
		针对特有的数据，可以先进行一步筛选，然后，在放到展示页面(changelist)去
		例如 ，客户表的课程顾问为空的时候
		:param request:
		:param args:
		:param kwargs:
		:return:
		"""
		return self.model_class.objects

	def changelist_view(self, request, *args, **kwargs):
		"""
		列表页面
		:param request:
		:return:
		"""
		################ 1.批量操作(处理Action 下拉框) #############
		action_list = self.get_action_list()
		action_dict = {func.__name__: func.text for func in
		               action_list}  # {'action_multi_delete':'批量删除','action_depart_multi_init':'批量初始化'}
		# 并且此时的multi_delete 是一个对象的名称
		if request.method == "POST":
			action_func_name = request.POST.get(
				"action")  # action_func_name,type(action_func_name),bool(action_func_name) = multi_init <class 'str'> True
			if action_func_name and action_func_name in action_dict:
				# <bound method UserInfoHandler.multi_delete of <app01.stark.UserInfoHandler object at ...>>
				action_response = getattr(self, action_func_name)(request, *args, **kwargs)
				if action_response:  # 如果调用的批量处理函数有返回值，则执行返回值
					return action_response
		################ 2.模糊搜索 #############
		"""
		1.如果search_list 中没有值,则不显示搜索框
		2.获取用户提交的关键字
		3.构造条件
		"""

		search_list = self.get_search_list()

		search_value = request.GET.get('q', '')
		from django.db.models import Q
		# Q　用于构造复杂的ORM查询条件
		conn = Q()
		conn.connector = 'OR'
		if search_value:
			for item in search_list:
				conn.children.append((item, search_value))

		################ 3.排序处理 #############
		order_list = self.get_order_list()

		################ 4.处理分页 #############
		# 数据库里面所有的数据
		# 获取组合搜索条件
		search_group_condition = self.get_search_group_condition(request)

		prev_queryset = self.get_queryset(request, *args, **kwargs)

		all_data = prev_queryset.filter(conn).filter(**search_group_condition).order_by(*order_list)

		query_params = request.GET.copy()  # copy方法是默认不能修改request.GET里面的参数的
		query_params._mutable = True  # 这样就可以修改request.GET 里面的参数值了

		pager = Pagination(
			current_page=request.GET.get('page'),  # 获取页面返回的获取的页码
			all_count=all_data.count(),  # 数据库里面所有数据的计算
			base_url=request.path_info,  # 访问的基础URL,例如 http://127.0.0.1/abc?name=ryan&age=18 里面的 /abc
			params=query_params,
			# 用户URL里面的参数,例如 http://127.0.0.1/abc?name=ryan&age=18里面的name=ryan&age=18,它是 QueryDict类型
			per_page_num=self.per_page_num  # 这个是每页显示的个数(扩展，可以在网页端输入，然后在传入服务器端)
		)

		# 列表展示页使用分页的设置 （切片的应用）
		data_list = all_data[pager.start:pager.end]

		################ 5.处理表格 #############
		list_display = self.get_list_display(request, *args, **kwargs)
		# 5.1 处理表头
		header_list = []
		if list_display:  # 如果有list_display(展示列) 就循环它
			for key_or_func in list_display:
				if isinstance(key_or_func, FunctionType):
					verbose_name = key_or_func(self, obj=None, is_header=True, )
				else:
					verbose_name = self.model_class._meta.get_field(key_or_func).verbose_name
				header_list.append(verbose_name)
		else:  # 如果没有list_display(展示列)，那么表头就是它的表名
			header_list.append(self.model_class._meta.model_name)

		# 5.2 处理表的内容
		# queryset[对象1，对象2]
		body_list = []

		for row in data_list:
			tr_list = []
			if list_display:
				for key_or_func in list_display:
					if isinstance(key_or_func, FunctionType):
						tr_list.append(key_or_func(self, row, False, *args, **kwargs))
					else:
						tr_list.append(getattr(row, key_or_func))  # obj.gender
			else:
				tr_list.append(row)
			body_list.append(tr_list)

		################ 6.添加按钮 #############
		add_btn = self.get_add_btn(request, *args, **kwargs)

		################ 添加批量上传按钮 ########
		import_excel_btn = self.get_import_excel_btn(request, *args, **kwargs)

		################ 7.组合搜索 #############
		search_group_row_list = []
		search_group = self.get_search_group()  # ['gender', 'depart']
		for option_object in search_group:
			row = option_object.get_queryset_or_tuple(self.model_class, request, *args, **kwargs)

			search_group_row_list.append(row)

		return render(request, self.change_list_template or 'stark/changelist.html', {
			'data_list': data_list,
			'header_list': header_list,
			'body_list': body_list,
			'pager': pager,
			'add_btn': add_btn,
			'import_excel_btn': import_excel_btn,
			'search_list': search_list,
			'search_value': search_value,
			'action_dict': action_dict,
			'search_group_row_list': search_group_row_list
		})

	def form_database_save(self, request, form, is_update, *args, **kwargs):  # 视频中的save
		"""
		在使用ModelForm保存数据之前，预留的钩子方法
		:param form:
		:param is_update:
		:return:
		"""
		form.save()

	def add_view(self, request, *args, **kwargs):
		"""
		添加页面
		:param request:
		:return:
		"""
		model_form_class = self.get_model_form_class(True, request, None, *args, **kwargs)
		if request.method == "GET":
			form = model_form_class()
			return render(request, self.add_template or 'stark/change.html', {"form": form})

		form = model_form_class(data=request.POST)
		if form.is_valid():
			response = self.form_database_save(request, form, False, *args, **kwargs)
			# 在数据库中保存成功后,跳转回列表页面（携带原来的参数）
			return response or redirect(self.reverse_list_url(*args, **kwargs))
		return render(request, self.add_template or 'stark/change.html', {"form": form})

	def get_change_object(self, request, pk, *args, **kwargs):
		return self.model_class.objects.filter(pk=pk).first()

	def change_view(self, request, pk, *args, **kwargs):
		"""
		编辑页面
		:param request:
		:return:
		"""
		# 当前编辑对象
		current_change_object = self.get_change_object(request, pk, *args, **kwargs)
		if not current_change_object:
			return HttpResponse("需要修改的对象不存在，请重新选择")

		model_form_class = self.get_model_form_class(False, request, pk, *args, **kwargs)
		if request.method == "GET":
			form = model_form_class(instance=current_change_object)
			return render(request, self.change_template or 'stark/change.html', {"form": form})

		form = model_form_class(data=request.POST, instance=current_change_object)
		if form.is_valid():
			response = self.form_database_save(request, form, True, *args, **kwargs)
			# 在数据库中保存成功后,跳转回列表页面（携带原来的参数）
			return response or redirect(self.reverse_list_url(*args, **kwargs))
		return render(request, self.change_template or 'stark/change.html', {"form": form})

	def delete_object(self, request, pk, *args, **kwargs):
		self.model_class.objects.filter(pk=pk).delete()

	def delete_view(self, request, pk, *args, **kwargs):
		"""
		删除页面
		:param request:
		:param pk:
		:return:
		"""
		origin_list_url = self.reverse_list_url(*args, **kwargs)
		if request.method == "GET":
			return render(request, self.delete_template or 'stark/delete.html', {'cancel': origin_list_url})
		response = self.delete_object(request, pk, *args, **kwargs)
		return response or redirect(origin_list_url)

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

	@property
	def get_import_excel_url_name(self):
		"""
		获取删除页面URL的name
		:return:
		"""
		return self.get_url_name('import')

	def reverse_commons_url(self, name, *args, **kwargs):
		name = "%s:%s" % (self.site.namespace, name)
		base_url = reverse(name, args=args, kwargs=kwargs)
		if not self.request.GET:
			add_url = base_url
		else:
			param = self.request.GET.urlencode()
			new_query_dict = QueryDict(mutable=True)
			new_query_dict['_filter'] = param
			add_url = "%s?%s" % (base_url, new_query_dict.urlencode())
		return add_url

	def reverse_add_url(self, *args, **kwargs):
		"""
		生成带有原搜索条件的添加URL
		:return:
		"""
		return self.reverse_commons_url(self.get_add_url_name, *args, **kwargs)

	def reverse_change_url(self, *args, **kwargs):
		"""
		生成带有原搜索条件的编辑URL
		:param args:
		:param kwargs:
		:return:
		"""
		return self.reverse_commons_url(self.get_change_url_name, *args, **kwargs)

	def reverse_delete_url(self, *args, **kwargs):
		"""
		生成带有原搜索条件的删除URL
		:param args:
		:param kwargs:
		:return:
		"""
		return self.reverse_commons_url(self.get_delete_url_name, *args, **kwargs)

	def reverse_list_url(self, *args, **kwargs):
		"""
		跳转回列表页面时，生成URL
		:return:
		"""
		name = "%s:%s" % (self.site.namespace, self.get_list_url_name)
		base_url = reverse(name, args=args, kwargs=kwargs)
		param = self.request.GET.get('_filter')
		if not param:
			return base_url
		print("------------->%s?%s" % (base_url, param))
		return "%s?%s" % (base_url, param)

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
			url(r'^delete/(?P<pk>\d+)/$', self.wrapper(self.delete_view), name=self.get_delete_url_name),
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

	def registry(self, model_class, handler_class=None, prev=None):
		"""

		:param model_class: 是调用此方法的app中的 models中相关的类  例如：models.UserInfo
		:param handler_calss: 处理请求的视图函数所在的类
		:param prev: 生成 url 的前缀
		:return:
		"""
		if not handler_class:
			handler_class = StarkHandler  # StarkHandler 就是上面创建的类

		self._registry.append(
			{'model_class': model_class, 'handler': handler_class(self, model_class, prev), 'prev': prev})
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
