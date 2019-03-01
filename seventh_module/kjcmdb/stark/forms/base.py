# -*- coding: utf-8 -*-

# __title__ = 'base.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.12.04'

from django import forms

class StarkModelForm(forms.ModelForm):
	# 统一给ModelForm生成的字段添加css 样式
	def __init__(self,*args,**kwargs):
		super(StarkModelForm,self).__init__(*args,**kwargs)
		for name,field in self.fields.items():
			field.widget.attrs['class'] = 'form-control'


class StarkForm(forms.Form):
	# 统一给ModelForm生成的字段添加css 样式
	def __init__(self,*args,**kwargs):
		super(StarkForm,self).__init__(*args,**kwargs)
		for name,field in self.fields.items():
			field.widget.attrs['class'] = 'form-control'














