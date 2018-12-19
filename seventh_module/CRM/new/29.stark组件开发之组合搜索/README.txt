视频  stark组件开发-组合搜索
https://www.cnblogs.com/wupeiqi/articles/9979155.html

组合搜索
	- 什么是组合搜索
	
	- 如何实现组合搜索？
		- 实现思路，根据字段找到其关联的数据; choice ,FK ,M2M
		
		- 第一步：配置
					# 组合搜索
					search_group = ['gender','depart']
					def get_search_group(self):
						return self.search_group
	
		- 第二步：根据配置获取关联数据
					################ 7.组合搜索 #############
					from django.db.models import  ForeignKey,ManyToManyField
					search_group = self.get_search_group()  # ['gender', 'depart']
					for item in search_group:
						# 根据gender或depart字符串，去自己对应的Model类中找到字段对象，
						field_object = self.model_class._meta.get_field(item)

						# 根据对象获取关联数据
						if isinstance(field_object,ForeignKey) or isinstance(field_object,ManyToManyField):
							# FK和M2M，应该获取其关联表中的数据
							# 根据表字段获取其关联表的所有数据 field_object.rel.model.objects.all()
							print("ForeignKey==>",field_object)
							print("关联的表",item,field_object.rel.model.objects.all())

						else:
							# 获取Choice中的数据
							print(item,"<===Choice==>",field_object.choices)
		
		- 第三步：根据配置获取关联数据（含条件）
			配置 app01/stark.py 的搜索条件
					# 组合搜索预留的搜索条件的钩子函数
					class MyOption(Option):
						def get_db_condition(self,request,*args,**kwargs):
							return {'id__gt':request.GET.get('nid')}
				
				
					class UserInfoHandler(StarkHandler):
						....
						# 组合搜索
						# search_group = ['gender','depart']
						search_group = {
							Option('gender'),
							MyOption('depart',{'id__gt': 2}),
						}
				
				stark/service/v1.py
					from django.db.models import  ForeignKey,ManyToManyField
					class Option(object):
						def __init__(self,field,db_condition=None):
							"""

							:param field: 组合搜索的字段
							:param db_condition: 数据库关联查询时的条件
							"""
							self.field = field
							if not db_condition:
								db_condition = {}
							else:
								self.db_condition = db_condition

						def get_db_condition(self,request,*args,**kwargs):
							return self.db_condition

						def get_queryset_or_tuple(self,model_class,request,*args,**kwargs):
							"""
							根据字段去获取数据库关联的数据
							:return:
							"""
							# 根据gender或depart字符串，去自己对应的Model类中找到字段对象，
							field_object = model_class._meta.get_field(self.field)

							# 根据对象获取关联数据
							if isinstance(field_object, ForeignKey) or isinstance(field_object, ManyToManyField):
								# FK和M2M，应该获取其关联表中的数据
								# 根据表字段获取其关联表的所有数据 field_object.rel.model.objects.all()
								db_condition = self.get_db_condition(request,*args,**kwargs)
								print("关联的表", self.field, field_object.rel.model.objects.filter(**db_condition))

							else:
								# 获取Choice中的数据
								print(self.field, "<===Choice==>", field_object.choices)
			
		
				v1.py/StarkHandler.py的方法中 changelist_view
						################ 7.组合搜索 #############
						search_group = self.get_search_group()  # ['gender', 'depart']
						for option_object in search_group:
							option_object.get_queryset_or_tuple(self.model_class,request,*args,**kwargs)
		
		
		- 第四步：在页面上显示组合搜索按钮
			- 将QuerySet 和元组进行封装
			
		- 第五步：为组合搜索按钮生成URL
			- 生成URl时不影响其他组的条件
			- 条件的筛选
			- 多选
		
		
		
		
		
总结：
	1.功能
		- 展示页面
		- 添加页面
		- 编辑页面
		- 删除页面
		
		- 模糊搜索(关键字)
		
		- 批量操作
		
		- 选择批量操作
		
		- 组合搜索
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		














