# -*- coding: utf-8 -*-

# __title__ = 'userinfo.py'
# __author__ = 'YangYang'
# __mtime__ = '2019.03.01'

from django.shortcuts import HttpResponse, render, redirect
from django.conf.urls import url
from django.utils.safestring import mark_safe
from stark.service.v1 import StarkHandler, get_choice_text
from asset import models

from asset.forms.user_form import UserInfoAddModelForm, UserInfoChangeModelForm, ResetPasswordForm


class UserInfoHandler(StarkHandler):


	def display_reset_pwd(self, obj=None, is_header=None, *args, **kwargs):
		if is_header:
			return "重置密码"
		reset_url = self.reverse_commons_url(self.get_url_name('reset_pwd'),pk=obj.pk)
		return  mark_safe('<a href="%s" class="btn btn-info btn-xs" >重置密码</a>' % reset_url)


	list_display = ['nickname', 'name', get_choice_text('性别', 'gender'), 'phone', 'email', 'depart',display_reset_pwd]

	# 定制添加和删除页面显示
	def get_model_form_class(self, is_add, request, pk, *args, **kwargs):

		if is_add:
			return UserInfoAddModelForm
		return UserInfoChangeModelForm

	def reset_password(self, request, pk):
		userinfo_object = models.UserInfo.objects.filter(id=pk).first()

		if not userinfo_object:
			return HttpResponse("用户不存在，无法进行重置")
		if request.method == "GET":
			form = ResetPasswordForm()
			return render(request, 'stark/change.html', {"form": form})

		form = ResetPasswordForm(data=request.POST)
		if form.is_valid():
			userinfo_object.password = form.cleaned_data['password']
			userinfo_object.save()
			return redirect(self.reverse_list_url())
		return render(request, 'stark/change.html', {"form": form})

	def extra_urls(self):
		patterns = [
			url(r'^reset/password/(?P<pk>\d+)/$', self.wrapper(self.reset_password),name=self.get_url_name('reset_pwd'))
		]
		return patterns
