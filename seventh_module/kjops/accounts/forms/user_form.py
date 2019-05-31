# -*- coding: utf-8 -*-

from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets

from stark.forms.base import StarkForm,StarkModelForm

from accounts import models
from accounts.utils.md5 import gen_md5

class UserInfoAddModelForm(StarkModelForm):
	confirm_passwd = forms.CharField(label='确认密码')
	class Meta:
		model = models.UserInfo
		fields = ['name','nickname','password','confirm_passwd','gender','email','status','depart','roles']

	def clean_confirm_passwd(self):
		password = self.cleaned_data['password']
		confirm_password = self.cleaned_data['confirm_passwd']
		if password != confirm_password:
			raise  ValidationError("密码输入不一致")
		elif len(password) < 6:
			raise ValidationError("密码长度不能小于6位")
		return confirm_password

	def clean(self):
		password = self.cleaned_data['password']
		self.cleaned_data['password'] = gen_md5(password)
		return self.cleaned_data

class UserInfoChangeModelForm(StarkModelForm):
	class Meta:
		model = models.UserInfo
		fields = ['name','nickname', 'gender', 'email', 'status', 'depart', 'roles']   # 可以调整字段显示顺序


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

