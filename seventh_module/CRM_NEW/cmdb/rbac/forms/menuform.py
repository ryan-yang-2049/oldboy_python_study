# -*- coding: utf-8 -*-



from django import forms
from rbac import  models
from django.utils.safestring import mark_safe
from rbac.forms.baseform import BaseForm


ICON_LIST = [
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
]



class MenuModelForm(forms.ModelForm):
	class Meta:
		model = models.Menu
		fields = ['title','icon']
		widgets = {
			'title':forms.TextInput(attrs={'class':'form-control'}),
			'icon':forms.RadioSelect(
				choices=ICON_LIST,
				attrs={'class':'clearfix'}

			)
		}


class SecondMenuModelForm(BaseForm):
	class Meta:
		model = models.Permission
		exclude = ['pid',]

class PermissionModelForm(BaseForm):
	class Meta:
		model = models.Permission
		fields = ['title','url','name']



class MultiAddPermissionForm(forms.Form):
	title = forms.CharField(
		widget=forms.TextInput(attrs={'class': "form-control"})
	)
	url = forms.CharField(
		widget=forms.TextInput(attrs={'class': "form-control"})
	)
	name = forms.CharField(
		widget=forms.TextInput(attrs={'class': "form-control"})
	)
	menu_id = forms.ChoiceField(
		choices=[(None, '-----')],
		widget=forms.Select(attrs={'class': "form-control"}),
		required=False,
	)
	pid_id = forms.ChoiceField(
		choices=[(None, '-----')],
		widget=forms.Select(attrs={'class': "form-control"}),
		required=False,
	)
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['menu_id'].choices += models.Menu.objects.values_list('id', 'title')
		self.fields['pid_id'].choices += models.Permission.objects.filter(pid__isnull=True).exclude(
			menu__isnull=True).values_list('id', 'title')



class MultiEditPermissionForm(forms.Form):
	id = forms.IntegerField(
		widget=forms.HiddenInput()
	)
	title = forms.CharField(
		widget=forms.TextInput(attrs={'class': "form-control"})
	)
	url = forms.CharField(
		widget=forms.TextInput(attrs={'class': "form-control"})
	)
	name = forms.CharField(
		widget=forms.TextInput(attrs={'class': "form-control"})
	)
	menu_id = forms.ChoiceField(
		choices=[(None, '-----')],
		widget=forms.Select(attrs={'class': "form-control"}),
		required=False,
	)
	pid_id = forms.ChoiceField(
		choices=[(None, '-----')],
		widget=forms.Select(attrs={'class': "form-control"}),
		required=False,
	)
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['menu_id'].choices += models.Menu.objects.values_list('id', 'title')
		self.fields['pid_id'].choices += models.Permission.objects.filter(pid__isnull=True).exclude(
			menu__isnull=True).values_list('id', 'title')






















