# -*- coding: utf-8 -*-


from django.core.exceptions import  ValidationError
from django import forms
from rbac import  models
from rbac.forms.baseform import BaseForm

class UserModelForm(BaseForm):
	confirm_password = forms.CharField(label='确认密码')
	class Meta:
		model = models.UserInfo
		fields = ['name','email','password','confirm_password']

	def clean_confirm_password(self):
		"""
		钩子方法，密码验证
		:return:
		"""
		password = self.cleaned_data['password']
		confirm_password = self.cleaned_data['confirm_password']

		if password != confirm_password:
			raise ValidationError('密码不一致！')

		return confirm_password


class UpdateUserModelForm(BaseForm):
	class Meta:
		model = models.UserInfo
		fields = ['name','email']


class ResetUserModelForm(BaseForm):
	confirm_password = forms.CharField(label='确认密码')
	class Meta:
		model = models.UserInfo
		fields = ['password','confirm_password']

	def clean_confirm_password(self):
		"""
		钩子方法，密码验证
		:return:
		"""
		password = self.cleaned_data['password']
		confirm_password = self.cleaned_data['confirm_password']

		if password != confirm_password:
			raise ValidationError('密码不一致！')

		return confirm_password

