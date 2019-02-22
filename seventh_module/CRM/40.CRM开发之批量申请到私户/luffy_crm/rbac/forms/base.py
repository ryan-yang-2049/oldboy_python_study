# -*- coding: utf-8 -*-

# __title__ = 'base.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.12.04'

from django import forms

class BootStrapMOdelForm(forms.ModelForm):
	# 统一给ModelForm生成的字段添加css 样式
	def __init__(self,*args,**kwargs):
		super(BootStrapMOdelForm,self).__init__(*args,**kwargs)
		for name,field in self.fields.items():
			field.widget.attrs['class'] = 'form-control'









