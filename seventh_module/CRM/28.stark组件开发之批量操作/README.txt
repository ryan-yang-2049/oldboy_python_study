视频  stark组件开发
https://www.cnblogs.com/wupeiqi/articles/9979155.html


1.排序 视频 81-82
	stark/service/v1.py
	StarkHandler(object):
		....
		order_list = [ ]
		def get_order_list(self):
			return self.order_list or ['id']   # -id 按照id降序

		def changelist_view(self, request):
			"""
			列表页面
			:param request:
			:return:
			"""
			################ 1.排序处理 #############
			order_list = self.get_order_list()

			################ 2.处理分页 #############
			# 数据库里面所有的数据
			all_data = self.model_class.objects.all().order_by(*order_list)	# 按照什么什么排序

2.模糊搜索 视频 83
	- 实现思路：
		在页面上设置form表单，搜索：以GET形式提交到后台。后台获取数据然后进行筛选过滤
		后端获取到关键字之后，根据定义的列进行查找（多列可以按照 “或” 进行查询）
	
	- ORM的　Q　对象来实现
		class UserInfoHandler(StarkHandler):
			# per_page_num = 3
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

			# order_list = ['name']

			# 姓名中含有关键字或邮箱中含有关键字 如果没有 __contains 就算精确查找
			search_list = ['name__contains','email__contains']		======> 注意这里，设置的模糊查询的字段。如果这里有才在页面展示以及设定模糊搜索的字段
			
			
		stark/service/v1.py
			StarkHandler(object):
				....
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
					...........
	
	
3.批量操作 视频 84-85
	- list 页面添加checkbox
		class StarkHandler(object):
			......

			def display_checkbox(self, obj=None, is_header=None):
				"""
				自定义页面显示CheckBox
				:param obj:
				:param is_header:
				:return:
				"""
				if is_header:
					return "选择"
				return mark_safe('<input type="checkbox" name="pk" value="%s"/>'%(obj.pk))
	- 生成批量操作的按钮
		class StarkHandler(object):
			......
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
			def changelist_view(self, request, *args, **kwargs):
				"""
				列表页面
				:param request:
				:return:
				"""
				################ 1.批量操作(处理Action 下拉框) #############
				action_list = self.get_action_list()
				action_dict = {func.__name__: func.text for func in action_list}  # {'multi_delete':'批量删除','multi_init':'批量初始化'}

				if request.method == "POST":
					action_func_name = request.POST.get(
						"action")  # action_func_name,type(action_func_name),bool(action_func_name) = multi_init <class 'str'> True
					if action_func_name and action_func_name in action_dict:
						# <bound method UserInfoHandler.multi_delete of <app01.stark.UserInfoHandler object at ...>>
						action_response = getattr(self, action_func_name)(request, *args, **kwargs)
						if action_response: # 如果调用的批量处理函数有返回值，则执行返回值
							return action_response
				.......
				
	class UserInfoHandler(StarkHandler):
		list_display = [StarkHandler.display_checkbox,	# checkbox
						'name',
						get_choice_text('性别', 'gender'),
						get_choice_text('班级', 'classes'),
						# 'gender','classes',
						'age', 'email', 'depart',
						StarkHandler.display_edit,
						StarkHandler.display_del]
		...
		
		def action_depart_multi_init(self, request, *args, **kwargs):
			"""
			批量初始化
			:param request:
			:return:
			"""
			pk_list = request.POST.getlist('pk')
			self.model_class.objects.filter(id__in=pk_list).update(depart_id=3)
		action_depart_multi_init.text = '部门初始化'

		# 批量操作的选项 。 如果没有值，那么页面就不显示
		action_list = [StarkHandler.action_multi_delete,action_depart_multi_init]	# 具有什么批量操作的功能
















