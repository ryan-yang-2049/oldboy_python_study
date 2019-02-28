# -*- coding: utf-8 -*-

# __title__ = 'userinfo.py'
# __author__ = 'YangYang'
# __mtime__ = '2019.02.21'

from django.shortcuts import HttpResponse, redirect, render
from django.utils.safestring import mark_safe
from django.conf.urls import url

from stark.service.v1 import StarkHandler, get_choice_text, Option
from web import models
from web.forms.user_form import UserInfoChangeModelForm, UserInfoAddModelForm, ResetPasswordForm
from web.views.base import PermissionHandler

class UserInfoHandler(PermissionHandler,StarkHandler):
	def display_reset_pwd(self, obj=None, is_header=None):
		if is_header:
			return "重置密码"
		reset_url = self.reverse_commons_url(self.get_url_name('reset_pwd'), pk=obj.pk)
		return mark_safe('<a href="%s">重置密码</a>' % reset_url)

	list_display = ['nickname', 'name', get_choice_text('性别', 'gender'), 'phone', 'email', 'depart', display_reset_pwd]

	def get_model_form_class(self, is_add=False,*args, **kwargs):
		"""
		定制添加和编辑页面
		:param is_add:
		:return:
		"""
		if is_add:
			return UserInfoAddModelForm
		return UserInfoChangeModelForm

	def reset_password(self, request, pk):
		"""
		重置密码的视图函数
		:param request:
		:param pk:
		:return:
		"""
		userinfo_object = models.UserInfo.objects.filter(id=pk).first()
		if not userinfo_object:
			return HttpResponse("用户不存在，无法进行重置！")
		if request.method == "GET":
			form = ResetPasswordForm()
			return render(request, 'stark/change.html', {'form': form})
		form = ResetPasswordForm(data=request.POST)
		if form.is_valid():
			userinfo_object.password = form.cleaned_data['password']
			userinfo_object.save()
			return redirect(self.reverse_list_url())
		return render(request, 'stark/change.html', {'form': form})

	def extra_urls(self):
		patterns = [
			url(r'^reset/password/(?P<pk>\d+)/$', self.wrapper(self.reset_password),
			    name=self.get_url_name('reset_pwd'))
		]

		return patterns

	# 模糊搜索
	search_list = ['nickname__contains', 'name__contains']

	# 组合搜索
	search_group = [
		Option(field='gender'),
		Option(field='depart', is_multi=True),
	]
