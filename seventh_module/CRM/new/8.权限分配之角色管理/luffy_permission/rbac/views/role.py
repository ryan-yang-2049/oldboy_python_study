# -*- coding: utf-8 -*-

# __title__ = 'role.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.11.29'

"""
角色管理
"""

from django.shortcuts import render,redirect,HttpResponse
from django import forms
from django.urls import reverse
from rbac import models

class RoleModelForm(forms.ModelForm):
	class Meta:         # https://blog.csdn.net/Leo062701/article/details/80963625
		model = models.Role
		fields = ['title',]

		widgets ={
			'title': forms.TextInput(attrs={'class':'form-control'})
		}


def role_list(request):
	"""
	角色列表
	:param request:
	:return:
	"""
	role_queryset = models.Role.objects.all()
	return render(request,'rbac/role_list.html',{'roles':role_queryset})

def role_add(requet):

	if requet.method == "GET":
		form = RoleModelForm()
		return render(requet,'rbac/role_add.html',{'form':form})

	form = RoleModelForm(data=requet.POST)
	if form.is_valid():
		form.save()
		return redirect(reverse('rbac:role_list'))

	return render(requet, 'rbac/role_add.html', {'form': form}) # 如果输入为空，则在form 中有errors的错误信息





