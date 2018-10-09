import functools
from types import  FunctionType,MethodType

from django.utils.safestring import mark_safe
from django.shortcuts import HttpResponse,redirect,render
from django.conf.urls import url
from django.urls import reverse

from django import forms

class StarkConfig(object):

	# checkbox
	def display_checkbox(self,row=None,header=False):
		"""
		row表示每一行数据，如果是表头则不用添加
		header=True时 那么表示是表头
		:param row:
		:param header:
		:return:
		"""
		if header == True:
			return  "选择"
		return mark_safe("<input type='checkbox' name='pk' value='%s'/>"%row.pk)

	def display_edit(self,row=None,header=False):
		"""
		row表示每一行数据，如果是表头则不用添加
		header=True时 那么表示是表头
		:param row:
		:param header:
		:return:
		"""
		if header == True:
			return  "编辑"

		return mark_safe('<a href="%s"><i class="fa fa-edit" aria-hidden="true"></i></a>"'%self.reverse_edit_url(row))
	def display_del(self,row=None,header=False):
		"""
		row表示每一行数据，如果是表头则不用添加
		header=True时 那么表示是表头
		:param row:
		:param header:
		:return:
		"""
		if header == True:
			return  "删除"

		return mark_safe('<a href="%s"><i class="fa fa-trash-o" aria-hidden="true"></i></a>"'%self.reverse_del_url(row))

	def display_edit_del(self,row=None,header=False):
		if header == True:
			return "操作"

		tpl = """
				<a href="%s"><i class="fa fa-edit" aria-hidden="true"></i></a>
				|
				<a href="%s"><i class="fa fa-trash-o" aria-hidden="true"></i></a>
		"""%(self.reverse_edit_url(row),self.reverse_del_url(row))
		return  mark_safe(tpl)

	order_by = []
	list_display = []       #表头
	model_form_class = None




	def __init__(self,model_class,site):
		self.model_class = model_class
		self.site = site




	def get_order_by(self):
		return self.order_by

	def get_list_display(self):

		return self.list_display


	def get_add_btn(self):

		return mark_safe('<a href="%s" class="btn btn-success">添加</a>'%self.reverse_add_url())

	def get_model_form_class(self):
		"""
		获取 ModelForm 类
		:return:
		"""

		if self.model_form_class:
			return self.model_form_class

		class AddModelForm(forms.ModelForm):
			class Meta:
				model = self.model_class
				fields = "__all__"
		return AddModelForm


	def changelist_view(self,request):
		"""
		所有URL的查看列表页面
		:param request:
		:return:
		"""
		questryset = self.model_class.objects.all().order_by(*self.get_order_by())

		############### 添加按钮 ###########
		add_btn = self.get_add_btn()

		# 处理表格
		# inclusion_tag
		# 生成器
		list_display = self.get_list_display()  # 表头：表格想要展示的信息
		header_list = []
		if list_display:
			for name_or_func in list_display:
				if isinstance(name_or_func,FunctionType):   # 如果是function函数，那么此时的 name_or_func 就是 f1 函数。
					header_list.append(name_or_func(self,header=True))
				else:
					header_list.append(self.model_class._meta.get_field(name_or_func).verbose_name)
		else:
			header_list.append(self.model_class._meta.model_name)

		body_list = []
		for row in questryset:
			row_list = []
			if not list_display:
				row_list.append(row)   # 此时的row是一个对象 ,例如：userinfo object，如果需要显示字符串，则用__str__ 在model里面，如果要展示 verbose_name 则需在对应app的stark里面的list_display 里面写上对应的字段

				body_list.append(row_list)
				continue

			for name_or_func in list_display:
				if isinstance(name_or_func,FunctionType):
					val = name_or_func(self,row=row)
				else:
					val = getattr(row,name_or_func)
				row_list.append(val)
			body_list.append(row_list)

		return render(request,'stark/changelist.html',locals())
	# return HttpResponse("change_list %s"%self.model_class._meta.app_label)

	def add_view(self,request):
		'''
		所有添加页面，都在此函数处理
		使用ModelForm实现
		:param request:
		:return:
		'''

		AddModelForm = self.get_model_form_class()
		if request.method == "GET":
			form = AddModelForm()
			return render(request, 'stark/change_form.html', locals())

		form = AddModelForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect(self.reverse_list_url())
		return render(request, 'stark/change_form.html', locals())


	def change_view(self,request,pk):
		"""
		所有得编辑页面
		:param request:
		:param pk:
		:return:
		"""
		obj = self.model_class.objects.filter(pk=pk).first()
		ModelFormClass = self.get_model_form_class()
		if not obj:
			return HttpResponse("不存在")
		if request.method == "GET":
			form = ModelFormClass(instance=obj)
			return render(request,'stark/change_form.html',locals())

		form = ModelFormClass(data=request.POST,instance=obj)
		if form.is_valid():
			form.save()
			return redirect(self.reverse_list_url())
		return render(request,'stark/change_form.html',locals())


	def delete_view(self,request,pk):
		"""
		所有删除页面
		:param request:
		:param pk:
		:return:
		"""
		cancel_url = self.reverse_list_url()
		if request.method == "GET":
			return render(request,'stark/delete.html',locals())


		self.model_class.objects.filter(pk=pk).delete()
		return redirect(self.reverse_list_url())
	def wrapper(self,func):
		@functools.wraps(func)
		def inner(*args, **kwargs):
			return func(*args, **kwargs)

		return inner

	def get_urls(self):
		info = self.model_class._meta.app_label,self.model_class._meta.model_name

		urlpatterns = [
			url(r'^list/$', self.wrapper(self.changelist_view),name="%s_%s_changelist"%info),
			url(r'^add/$',  self.wrapper(self.add_view),name="%s_%s_add"%info),
			url(r'^(?P<pk>\d+)/change/',  self.wrapper(self.change_view),name="%s_%s_change"%info),
			url(r'^(?P<pk>\d+)/del/$',  self.wrapper(self.delete_view),name="%s_%s_del"%info),
		]

		extra = self.extra_url()
		if extra:
			urlpatterns.extend(extra)

		return urlpatterns

	def extra_url(self):
		pass

	def reverse_list_url(self):
		app_label = self.model_class._meta.app_label
		model_name = self.model_class._meta.model_name

		namespace = self.site.namespace
		name = "%s:%s_%s_changelist" % (namespace,app_label,model_name)
		list_url = reverse(name)
		return list_url

	def reverse_add_url(self):
		app_label = self.model_class._meta.app_label
		model_name = self.model_class._meta.model_name

		namespace = self.site.namespace
		name = "%s:%s_%s_add" % (namespace,app_label,model_name)
		edit_url = reverse(name)
		return edit_url

	def reverse_edit_url(self,row):
		app_label = self.model_class._meta.app_label
		model_name = self.model_class._meta.model_name

		namespace = self.site.namespace
		name = "%s:%s_%s_change" % (namespace,app_label,model_name)
		edit_url = reverse(name,kwargs={'pk':row.pk})
		return edit_url

	def reverse_del_url(self,row):
		app_label = self.model_class._meta.app_label
		model_name = self.model_class._meta.model_name

		namespace = self.site.namespace
		name = "%s:%s_%s_del" % (namespace,app_label,model_name)
		del_url = reverse(name,kwargs={'pk':row.pk})
		return del_url
	@property
	def urls(self):
		return self.get_urls()

class AdminSite(object):
	def __init__(self):
		self._registry = {}
		self.app_name = 'stark'
		self.namespace = 'stark'

	def register(self,model_class,stark_config=None):

		if not stark_config:
			stark_config = StarkConfig
		self._registry[model_class] = stark_config(model_class,self)

		"""
		{
			models.UserInfo : StarkConfig(models.UserInfo), # 封装：model_class = UserInfo,site=site对象
			models.Role : RoleConfig(models.Role),          # 封装：model_class = Role,site=site对象
		}

		#
		# for k,v in self._registry.items():
		# 	# print(k,v.model_class,v.site)
		# 	v.run()
		"""

	def x1(self,request):
		return HttpResponse("stark x1")

	def x2(self,request):
		return HttpResponse("stark x2")

	def get_urls(self):
		urlpatterns = []
		# urlpatterns.append(url(r'^x1/',self.x1))
		# urlpatterns.append(url(r'^x2/',self.x2))
		# urlpatterns.append(url(r'^x3/',([
		#                               url(r'^add/',self.x1),
		#                               url(r'^change/',self.x1),
		#                               url(r'^del/',self.x1),
		#                               url(r'^edit/',self.x1),
		# ],None,None)))


		for k,v in self._registry.items():
			# k = models.UserInfo v=StarkConfig(models.UserInfo), # 封装：model_class = UserInfo,site=site对象
			# k = models.Role v = RoleConfig(models.Role),          # 封装：model_class = Role,site=site对象

			app_label = k._meta.app_label
			model_name = k._meta.model_name
			urlpatterns.append(url(r'^%s/%s/'%(app_label,model_name),(v.urls,None,None)))

			pass
		return urlpatterns

	@property
	def urls(self):
		return self.get_urls(),self.app_name,self.namespace

site = AdminSite()







