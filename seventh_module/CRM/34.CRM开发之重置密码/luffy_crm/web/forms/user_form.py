# -*- coding: utf-8 -*-

# __title__ = 'user_form.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.12.24'

from django import forms
from django.core.exceptions import  ValidationError


from stark.forms.base import StarkModelForm,StarkForm
from web import models
from web.utils.md5 import gen_md5

class UserInfoAddModelForm(StarkModelForm):
	confirm_password = forms.CharField(label='确认密码')
	class Meta:
		model = models.UserInfo
		fields = ['name','password','confirm_password','nickname','gender','phone','email','depart','roles']   # 可以调整字段显示顺序

	def clean_confirm_password(self):
		password = self.cleaned_data['password']
		confirm_password = self.cleaned_data['confirm_password']
		if password != confirm_password:
			raise ValidationError("密码输入不一致")
		return confirm_password

	def clean(self):    # 给密码加密
		password = self.cleaned_data['password']
		self.cleaned_data['password'] = gen_md5(password)
		return self.cleaned_data

class UserInfoChangeModelForm(StarkModelForm):
	confirm_password = models
	class Meta:
		model = models.UserInfo
		fields = ['name','nickname','gender','phone','email','depart','roles']   # 可以调整字段显示顺序

class ResetPasswordForm(StarkForm):
	password = forms.CharField(label='密码',widget=forms.PasswordInput)
	confirm_password = forms.CharField(label="重置密码",widget=forms.PasswordInput)

	def clean_confirm_password(self):
		password = self.cleaned_data['password']
		confirm_password = self.cleaned_data['confirm_password']
		if password != confirm_password:
			raise ValidationError("密码输入不一致")
		return confirm_password

	def clean(self):    # 给密码加密
		password = self.cleaned_data['password']
		self.cleaned_data['password'] = gen_md5(password)

		return self.cleaned_data


