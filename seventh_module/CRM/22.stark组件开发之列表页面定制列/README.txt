视频 71-74  定制页面显示的列
1.初级版
	def changelist_view(self, request):
		"""
		列表页面
		:param request:
		:return:
		"""
		# 1.处理表头
		# 访问：http://127.0.0.1:8000/stark/app01/userinfo/list/
		# 页面上要显示的列,以用户表为例：['name', 'age', 'email']
		print(self.list_display)
		# 用户访问的表 app01.models.UserInfo
		header_list = []
		for key in self.list_display:
			verbose_name = self.model_class._meta.get_field(key).verbose_name
			header_list.append(verbose_name)

		# 2.处理表的内容
		# queryset[对象1，对象2]
		data_list = self.model_class.objects.all()
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
			for key in self.list_display:
				tr_list.append(getattr(row, key))
			body_list.append(tr_list)

		return render(request, 'stark/changelist.html', locals())



	代码解释：以app01.models.UserInfo 为例
		解释1：
			self.model_class._meta.get_field('name') 相当于是 拿到了 app01.models.UserInfo 下面的name字段的对象就拿到了
			name_verbose_name = self.model_class._meta.get_field('name').verbose_name
			age_verbose_name = self.model_class._meta.get_field('age').verbose_name

	提示2：反射很重要，有时间在强记反射 getattr

2.进阶版: 没有自己的Hangler(表示没有自己的list_display)
	def changelist_view(self, request):
		"""
		列表页面
		:param request:
		:return:
		"""
		# 1.处理表头
		header_list = []
		if self.list_display:
			for key in self.list_display:
				verbose_name = self.model_class._meta.get_field(key).verbose_name
				header_list.append(verbose_name)
		else:
			header_list.append(self.model_class._meta.model_name)

		# 2.处理表的内容
		# queryset[对象1，对象2]
		data_list = self.model_class.objects.all()
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
			if self.list_display:
				for key in self.list_display:
					tr_list.append(getattr(row, key))
			else:
				tr_list.append(row)
			body_list.append(tr_list)

		return render(request, 'stark/changelist.html', locals())

	表示：如果没有定义自己的Handler 那么，就没有自己的 list_display,但是基类里面默认的list_display 为空。
		因此，如果没有自己的list_display 那么就默认展示为：表头为”表名称“，数据为表的对象 (__str__)
		表头：header_list.append(self.model_class._meta.model_name)
		数据：tr_list.append(row)


3.页面预留钩子函数
	根据用户角色的不同展示不同的列
	以UserInfo 为例

	stark/service/v1.py/StarkHandler
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

			list_display = self.get_list_display()

			# 1.处理表头
			header_list = []
			if list_display:
				for key in list_display:
					verbose_name = self.model_class._meta.get_field(key).verbose_name
					header_list.append(verbose_name)
			else:
				header_list.append(self.model_class._meta.model_name)

			# 2.处理表的内容
			# queryset[对象1，对象2]
			data_list = self.model_class.objects.all()
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
					for key in list_display:
						tr_list.append(getattr(row, key))
				else:
					tr_list.append(row)
				body_list.append(tr_list)

			return render(request, 'stark/changelist.html', locals())

		app01/stark.py
			class UserInfoHandler(StarkHandler):
				# 定制页面的列
				list_display = ['name', 'age', 'email']
				def get_list_display(self):
					"""
					自定义扩展，例如：根据用户角色的不同展示不同的列
					:return:
					"""
					return ['id','name','age']
			site.registry(models.UserInfo, UserInfoHandler)

		结果：根据 get_list_display() 这个预留的钩子函数，然后，就可以设置根据角色的不同展示不同的列。
			例如: 现在的UserInfo 就只展示了 id,name,age 3个字段

		提示：这个在后面和rbac配合使用的时候就会有大用

4.列表页面自定义函数扩展
class UserInfoHandler(StarkHandler):

	def display_edit(self, obj=None, is_header=None):
		"""
		自定义页面显示的列(表头和内容)
		:param obj: obj是列的数据对象，例如  obj.name
		:param is_header: 使用的时候判断是否是表头
		:return:
		"""
		if is_header:
			return "操作"
		return mark_safe('<a href="https://www.baidu.com">编辑</a>')

	def display_del(self, obj=None, is_header=None):
		"""
		自定义页面显示的列(表头和内容)
		:param obj: obj是列的数据对象，例如  obj.name
		:param is_header: 使用的时候判断是否是表头
		:return:
		"""
		if is_header:
			return "删除"
		return mark_safe('<a href="https://www.baidu.com">删除</a>')


	# 定制页面的列
	list_display = ['name', 'age', 'email', display_edit,display_del]


def changelist_view(self, request):
	"""
	列表页面
	:param request:
	:return:
	"""

	list_display = self.get_list_display()

	# 1.处理表头
	header_list = []
	if list_display:    # 如果有list_display(展示列) 就循环它
		for key_or_func in list_display:
			if isinstance(key_or_func,FunctionType):
				verbose_name = key_or_func(self,obj=None,is_header=True)
			else:
				verbose_name = self.model_class._meta.get_field(key_or_func).verbose_name
			header_list.append(verbose_name)
	else:   # 如果没有list_display(展示列)，那么表头就是它的表名
		header_list.append(self.model_class._meta.model_name)

	# 2.处理表的内容
	# queryset[对象1，对象2]
	data_list = self.model_class.objects.all()
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
				if isinstance(key_or_func,FunctionType):
					tr_list.append(key_or_func(self,obj=row,is_header=False))

				else:
					tr_list.append(getattr(row, key_or_func))
		else:
			tr_list.append(row)
		body_list.append(tr_list)

	return render(request, 'stark/changelist.html', locals())




5.方法和函数的区分
class Foo(object):

	def func(self,name):
		print(name)

obj = Foo()
# obj.func('ryan') # 方法
print(obj.func) # <bound method Foo.func of <__main__.Foo object at 0x105f7c5f8>>

# obj = Foo()
# Foo.func(obj,'ryan') # 函数
print(Foo.func) # <function Foo.func at 0x1060cb6a8>

























