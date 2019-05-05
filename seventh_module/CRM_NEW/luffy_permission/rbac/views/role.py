# -*- coding: utf-8 -*-
# 角色管理

from  django.shortcuts import HttpResponse,render,redirect
from django.urls import reverse

from rbac.forms.roleform import RoleModelForm
from rbac import  models



def role_list(request):
	"""
	角色列表
	:param request:
	:return:
	"""
	role_queryset = models.Role.objects.all()
	return render(request,'rbac/role_list.html',{'roles':role_queryset})

def role_add(request):
	"""
	添加角色
	:param request:
	:return:
	"""
	if request.method == "GET":
		form = RoleModelForm()
		return render(request, 'rbac/change.html', {'form':form})
	form = RoleModelForm(request.POST)
	if form.is_valid():
		form.save()
		return redirect(reverse('rbac:role_list'))
	return render(request, 'rbac/change.html', {'form': form})


def role_edit(request,pk):
	"""
	编辑角色
	:param request:
	:param pk:
	:return:
	"""
	obj = models.Role.objects.filter(pk=pk).first()
	if not obj:
		return HttpResponse("角色不存在")

	if request.method == "GET":
		form = RoleModelForm(instance=obj)  # 传到页面的时候，会自带查到的值
		return render(request, 'rbac/change.html', {'form':form})

	form = RoleModelForm(instance=obj,data=request.POST)
	if form.is_valid():
		form.save()
		return redirect(reverse('rbac:role_list'))
	return render(request, 'rbac/change.html', {'form':form})




def role_del(request,pk):
	"""
	删除角色
	:param request:
	:param pk:
	:return:
	"""
	origin_url = reverse('rbac:role_list')

	if request.method == "GET":
		info = models.Role.objects.filter(pk=pk).first()
		return render(request,'rbac/delete.html',{'info':info,"cancel":origin_url})

	models.Role.objects.filter(pk=pk).delete()
	return redirect(origin_url)





