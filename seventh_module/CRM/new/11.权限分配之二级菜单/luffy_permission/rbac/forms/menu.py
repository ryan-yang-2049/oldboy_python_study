# -*- coding: utf-8 -*-

# __title__ = 'menu.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.12.04'


from django import forms
from django.utils.safestring import mark_safe

from rbac import models

class MenuModelForm(forms.ModelForm):

	class Meta:
		model = models.Menu
		fields = ['title','icon']
		widgets = {
			'title':forms.TextInput(attrs={'class':'form-control'}),
			'icon' :forms.RadioSelect(
				choices=[
					['fa-calendar-plus-o',mark_safe('<i class="fa fa-calendar-plus-o" aria-hidden="true"></i>')],
					['fa-calendar-times-o',mark_safe('<i class="fa fa-calendar-times-o" aria-hidden="true"></i>')],
					['fa-bug',mark_safe('<i class="fa fa-bug" aria-hidden="true"></i>')],
					['fa-bookmark-o',mark_safe('<i class="fa fa-bookmark-o" aria-hidden="true"></i>')],
					['fa-bus',mark_safe('<i class="fa fa-bus" aria-hidden="true"></i>')],
					['fa-cogs',mark_safe('<i class="fa fa-cogs" aria-hidden="true"></i>')],
					['fa-copyright',mark_safe('<i class="fa fa-copyright" aria-hidden="true"></i>')],
					['fa-envelope-open',mark_safe('<i class="fa fa-envelope-open" aria-hidden="true"></i>')],
					['fa-crosshairs',mark_safe('<i class="fa fa-crosshairs" aria-hidden="true"></i>')],
					['fa-flag',mark_safe('<i class="fa fa-flag" aria-hidden="true"></i>')],
					['fa-image',mark_safe('<i class="fa fa-image" aria-hidden="true"></i>')],
					['fa-life-ring',mark_safe('<i class="fa fa-life-ring" aria-hidden="true"></i>')],
					['fa-pie-chart',mark_safe('<i class="fa fa-pie-chart" aria-hidden="true"></i>')],
					['fa-road',mark_safe('<i class="fa fa-road" aria-hidden="true"></i>')],
				],
				attrs={'class':'clearfix'}
			)
		}




