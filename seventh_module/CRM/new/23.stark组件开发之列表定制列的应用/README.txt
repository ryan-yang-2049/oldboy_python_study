视频 stark组件开发之列表定制列的应用
1.app01/models.py
	class UserInfo(models.Model):
		"""
		用户表
		"""
		name = models.CharField(verbose_name='姓名', max_length=32)
		gender_choices = (
			(1, '男'),
			(2, '女'),
		)
		gender = models.IntegerField(verbose_name='性别', choices=gender_choices, default=1)

		classes_choice = (
			(11, '全栈1期'),
			(21, '全栈3期'),
		)
		classes = models.IntegerField(verbose_name='班级', choices=classes_choice, default=11)
		age = models.CharField(verbose_name='年龄', max_length=32)
		email = models.CharField(verbose_name='邮箱', max_length=32)
		depart = models.ForeignKey(verbose_name='部门', to=Depart)

		def __str__(self):
			return self.name




2.app01/stark.py
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



	site.registry(models.UserInfo, UserInfoHandler)

3.stark/service/v1.py
	def get_choice_text(title, field):
		"""
		对于Stark组件中定义列时，choice如果想要显示中文信息，调用此方法即可。
		:param title: 希望页面显示的表头
		:param field: 字段名称 (例如：男女，班级等)
		:return:
		"""
		def inner(self, obj=None, is_header=None):
			if is_header:
				return title
			method = "get_%s_display" % field
			return getattr(obj, method)()
		return inner


	class StarkHandler(object):
		list_display = []
		per_page_num = 10
		def __init__(self,site,model_class, prev):
			self.site = site
			self.model_class = model_class  # 此时的model_class 是一个对象
			self.prev = prev  # 表示别名

		def display_edit(self, obj=None, is_header=None):
			"""
			自定义页面显示的列（表头和内容）
			:param obj:
			:param is_header:
			:return:
			"""
			if is_header:
				return "编辑"
			name = "%s:%s" % (self.site.namespace, self.get_change_url_name,)
			return mark_safe('<a href="%s">编辑</a>' % reverse(name, args=(obj.pk,)))

		def display_del(self, obj=None, is_header=None):
			if is_header:
				return "删除"
			name = "%s:%s" % (self.site.namespace, self.get_delete_url_name,)
			return mark_safe('<a href="%s">删除</a>' % reverse(name, args=(obj.pk,)))










