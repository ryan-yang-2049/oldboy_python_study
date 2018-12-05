from django.shortcuts import render
from django import forms

from app01 import models
# Create your views here.



class MultiPermissionForm(forms.Form):
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




def mutli_add(request):
	"""
	批量添加
	:param request:
	:return:
	"""

	if request.method == 'GET':
		formset = formset_class()
		return render(request, 'multi_add.html', {'formset': formset})






