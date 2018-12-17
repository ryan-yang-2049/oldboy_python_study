视频 77  stark组件开发之添加按钮显示和URL
https://www.cnblogs.com/wupeiqi/articles/9979155.html

1.添加页面的功能
	1.用户可以自定义定制
	2.预留钩子函数，权限的判断。
	

2.添加按钮的钩子函数以及自定义
			has_add_btn = True  # 是否具有添加按钮
			# 添加按钮的钩子函数
			def get_add_btn(self):
				if self.has_add_btn:
					return '<a class="btn btn-primary">添加</a>'
				return None



		自定制显示样式以及有无添加按钮
		class UserInfoHandler(StarkHandler):
			per_page_num = 1
			# 定制页面的列
			list_display = ['name',
							get_choice_text('性别', 'gender'),
							get_choice_text('班级', 'classes'),
							# 'gender','classes',
							'age', 'email', 'depart',
							StarkHandler.display_edit,
							StarkHandler.display_del]
			has_add_btn = True
			def get_add_btn(self):
				if self.has_add_btn:
					pass
				return None


3.添加按钮的URL

	def get_add_btn(self):
		if self.has_add_btn:
			# 根据别名反向生成URL
			return '<a class="btn btn-primary" href="%s">添加</a>'%(self.reverse_add_url())
		return None


	def reverse_add_url(self):
		name = "%s:%s" % (self.site.namespace, self.get_add_url_name)
		base_url = reverse(name)

		if not self.request.GET:
			add_url = base_url
		else:
			param = self.request.GET.urlencode()
			new_query_dict = QueryDict(mutable=True)
			new_query_dict['_filter'] = param
			add_url = "%s?%s" % (base_url, new_query_dict.urlencode())
		return add_url

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
重点：给所有的url都增加一个全局的request（意思就是，只要访问一次url就有一个全局的request）
	def wrapper(self,func):
		@functools.wraps(func)  # 保留原函数的源信息
		def inner(request,*args,**kwargs):
			self.request = request
			return func(request,*args,**kwargs)
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


++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
		
		
4.添加页面进行添加数据

	4.1 写了一个保留搜索条件的utils
	
		from django.urls import reverse
		from django.http import QueryDict

		class ParseUrl(object):
			"""
			保留原搜索条件
			"""

			def __init__(self,request,namespace,name):
				self.request = request
				self.namespace= namespace
				self.name = name
				self.nameinfo = "%s:%s"%(self.namespace,self.name)

			def memory_reverse_url(self):
				"""
				保留搜索的url参数到新的页面
				:return:
				"""
				base_url = reverse(self.nameinfo)
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
				base_url = reverse(self.nameinfo)
				params = self.request.GET.get("_filter")
				if not params:
					return base_url
				url = "%s?%s"%(base_url,params)
				return url


	4.2 设置所有表的动态的ModelForm，并集成基类的样式
		stark/form/base.py
			from django import forms

			class StarkModelForm(forms.ModelForm):
				# 统一给ModelForm生成的字段添加css 样式
				def __init__(self,*args,**kwargs):
					super(StarkModelForm,self).__init__(*args,**kwargs)
					for name,field in self.fields.items():
						field.widget.attrs['class'] = 'form-control'
		
		stark/service/v1.py 下StarkHandler的方法

			model_form_class = None	# 这里主要是用于预留的钩子，用于对象自己定制自己的ModelForm

			def get_model_form_class(self):
				if self.model_form_class:
					return self.model_form_class
				else:
					class DynamicModelForm(StarkModelForm):
						class Meta:
							model = self.model_class
							fields = '__all__'

				return DynamicModelForm


		例如UserInfo 
			class UserInfoModelForm(StarkModelForm):
				# xx = forms.CharField()  # 新增一个字段
				class Meta:
					model= models.UserInfo
					fields = "__all__"
					exclude = ["depart"]	# 减少一个字段
					
			class UserInfoHandler(StarkHandler):
				per_page_num = 1
				# 定制页面的列
				list_display = ['name',
								get_choice_text('性别', 'gender'),
								get_choice_text('班级', 'classes'),
								# 'gender','classes',
								'age', 'email', 'depart',
								StarkHandler.display_edit,
								StarkHandler.display_del]
				has_add_btn = True
				
				# 在stark/service/v1 下面定义了一个model_form_class的None，就是为了可以自定义自己的ModelForm
				model_form_class = UserInfoModelForm
				# 当页面减少了部门字段以后，数据库保存不了，因此，就要使用form_database_save的这个钩子函数，去自定义部门字段的值
				def form_database_save(self,form,is_update=False):
					form.instance.depart_id= 1	
					form.save()
			site.registry(models.UserInfo, UserInfoHandler)	
































