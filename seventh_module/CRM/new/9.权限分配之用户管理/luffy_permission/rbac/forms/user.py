# -*- coding: utf-8 -*-

# __title__ = 'user.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.11.30'

from django.core.exceptions import ValidationError
from django import forms
from rbac import models

class UserModelForm(forms.ModelForm):
	# 新增一个字段
	confirm_password = forms.CharField(label='确认密码')

	class Meta:
		model = models.UserInfo
		fields = ['name','password','confirm_password','email']

	# 统一给ModelForm生成的字段添加css 样式
	def __init__(self,*args,**kwargs):
		super(UserModelForm,self).__init__(*args,**kwargs)
		for name,field in self.fields.items():
			field.widget.attrs['class'] = 'form-control'


	def clean_confirm_password(self):
		"""
		检测密码是否一致
		:return:
		"""
		password = self.cleaned_data['password']
		confirm_password = self.cleaned_data['confirm_password']

		if password != confirm_password:
			raise ValidationError("密码输入不一致")

		# return self.cleaned_data  # 也可以这样返回
		return confirm_password


class UpdateUserModelForm(forms.ModelForm):

	class Meta:
		model = models.UserInfo
		fields = ['name','email']

	# 统一给ModelForm生成的字段添加css 样式
	def __init__(self,*args,**kwargs):
		super(UpdateUserModelForm,self).__init__(*args,**kwargs)
		for name,field in self.fields.items():
			field.widget.attrs['class'] = 'form-control'


class PasswordUserModelForm(forms.ModelForm):

	class Meta:
		model = models.UserInfo
		fields = ['name','email']

	# 统一给ModelForm生成的字段添加css 样式
	def __init__(self,*args,**kwargs):
		super(PasswordUserModelForm,self).__init__(*args,**kwargs)
		for name,field in self.fields.items():
			field.widget.attrs['class'] = 'form-control'