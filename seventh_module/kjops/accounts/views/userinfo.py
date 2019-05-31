# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.shortcuts import HttpResponse, render, redirect
from django.utils.safestring import mark_safe
from stark.service.v1 import StarkHandler, get_choice_text,Option
from accounts import models
from accounts.forms.user_form import UserInfoAddModelForm, UserInfoChangeModelForm, ResetPasswordForm


class UserInfoHandler(StarkHandler):

	def display_reset_pwd(self, obj=None, is_header=None, *args, **kwargs):
		if is_header:
			return "重置密码"

		reset_url = self.reverse_commons_url(self.get_url_name('reset_pwd'), pk=obj.pk)
		return mark_safe('<a class="btn btn-small btn-info" href="%s">重置密码</a>' % reset_url)



	list_display = ['name', 'nickname', 'email', 'depart', get_choice_text('状态', 'status'), display_reset_pwd]

	def get_model_form_class(self, is_add, request, pk, *args, **kwargs):
		"""
		定制添加和编辑页面
		:param is_add:
		:param request:
		:param pk:
		:param args:
		:param kwargs:
		:return:
		"""
		if is_add:
			return UserInfoAddModelForm
		return UserInfoChangeModelForm

	def reset_password(self, request, pk):
		"""
		重置密码
		:param request:
		:param pk: 重置密码的 用户ID
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
			url(r'^reset/password/(?P<pk>\d+)/$', self.wrapper(self.reset_password),name=self.get_url_name('reset_pwd'))
		]
		return patterns

	search_list = ['name__contains','nickname__contains','email_contains']
	search_group = [
		Option(field='depart')
	]