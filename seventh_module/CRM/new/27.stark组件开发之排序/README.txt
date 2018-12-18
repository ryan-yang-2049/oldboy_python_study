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

2.模糊搜索
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
	
	

3.批量操作




4.组合搜索

















