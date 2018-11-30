# -*- coding: utf-8 -*-

# __title__ = 'role.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.11.29'

"""
角色管理
"""

from django.shortcuts import render,redirect,HttpResponse

from django.urls import reverse
from rbac import models
from rbac.forms.role import RoleModelForm



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
		return render(requet, 'rbac/role_change.html', {'form':form})

	form = RoleModelForm(data=requet.POST)
	if form.is_valid():
		form.save()
		return redirect(reverse('rbac:role_list'))

	return render(requet, 'rbac/role_change.html', {'form': form}) # 如果输入为空，则在form 中有errors的错误信息


def role_edit(request,pk):
	"""
	编辑角色
	:param request:
	:param pk: 要修改的角色ID
	:return:
	"""
	obj = models.Role.objects.filter(id=pk).first()
	if not obj:
		return HttpResponse("角色不存在")


	if request.method == "GET":
		form = RoleModelForm(instance=obj)

		return render(request, 'rbac/role_change.html', {"form":form})

	form = RoleModelForm(instance=obj,data=request.POST)
	if form.is_valid():
		form.save()
		return redirect(reverse('rbac:role_list'))

	return render(request, 'rbac/role_change.html', {"form": form})


def role_del(request,pk):
	"""
	删除角色
	:param request:
	:param pk: 要删除的角色ID
	:return:
	"""

	origin_url = reverse('rbac:role_list')
	if request.method == "GET":

		return render(request,'rbac/role_delete.html',{"cancel":origin_url})

	models.Role.objects.filter(id=pk).delete()
	return redirect(origin_url)