# -*- coding: utf-8 -*-

# __title__ = 'stark.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.12.14'

from stark.forms.base import StarkModelForm
from stark.service.v1 import site, StarkHandler, get_choice_text,Option
from app01 import models


class DepartHandler(StarkHandler):
	list_display = ['id', 'title', StarkHandler.display_edit, StarkHandler.display_del]
	has_add_btn = True
	per_page_num = 2


# site.registry(models.Depart, DepartHandler, prev='public01')
site.registry(models.Depart, DepartHandler)


class UserInfoModelForm(StarkModelForm):
	# xx = forms.CharField()  # 新增一个字段  比如 密码和确认密码
	class Meta:
		model = models.UserInfo
		fields = "__all__"
	# exclude = ["depart"]

# 组合搜索预留的搜索条件的钩子函数
# class MyOption(Option):
# 	def get_db_condition(self,request,*args,**kwargs):
# 		return {'id__gt':request.GET.get('nid')}



class UserInfoHandler(StarkHandler):
	# per_page_num = 2
	# 定制页面的列
	list_display = [StarkHandler.display_checkbox,
	                'name',
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
	search_list = ['name__contains', 'email__contains']



	# 批量操作的选项 。 如果没有值，那么页面就不显示
	action_list = [StarkHandler.action_multi_delete, StarkHandler.action_depart_multi_init]  # 具有什么批量操作的功能

	# 组合搜索
	# search_group = ['gender','depart']
	search_group = {
		Option('gender'),
		Option('depart',is_multi=True,db_condition={'id__gt': 0}),
		Option('classes',is_multi=True,db_condition={'id__gt': 0}),
		# MyOption('depart',{'id__gt': 2}),
	}




	# 当页面减少了部门字段以后，数据库保存不了，因此，就要使用form_database_save的这个钩子函数，去自定义部门字段的值
	# def form_database_save(self, form, is_update=False):
	# 	form.instance.depart_id = 1
	# 	form.save()


site.registry(models.UserInfo, UserInfoHandler)


############# Deploy 表操作 #################
class DeployHandler(StarkHandler):
	list_display = [StarkHandler.display_checkbox, 'title', get_choice_text('状态', 'status'), StarkHandler.display_edit,
	                StarkHandler.display_del]
	# has_add_btn = False
	action_list = [StarkHandler.action_multi_delete]


site.registry(models.Deploy, DeployHandler)
