# -*- coding: utf-8 -*-

# __title__ = 'role.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.11.30'

from django import forms
from rbac import models
class RoleModelForm(forms.ModelForm):
	class Meta:         # https://blog.csdn.net/Leo062701/article/details/80963625
		model = models.Role
		fields = ['title',]

		widgets ={
			'title': forms.TextInput(attrs={'class':'form-control'})
		}







