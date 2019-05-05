# -*- coding: utf-8 -*-
# 角色管理

from  django.shortcuts import HttpResponse,render,redirect
from django.urls import reverse

from rbac.forms.userform import UserModelForm,UpdateUserModelForm,ResetUserModelForm

from rbac import  models



def user_list(request):
	"""
	角色列表
	:param request:
	:return:
	"""
	user_queryset = models.UserInfo.objects.all()
	return render(request,'rbac/user_list.html',{'users':user_queryset})

def user_add(request):
	"""
	添加用户
	:param request:
	:return:
	"""
	if request.method == "GET":
		form = UserModelForm()
		return render(request, 'rbac/change.html', {'form':form})
	form = UserModelForm(request.POST)
	if form.is_valid():
		form.save()
		return redirect(reverse('rbac:user_list'))
	return render(request, 'rbac/change.html', {'form': form})


def user_edit(request,pk):
	"""
	编辑角色
	:param request:
	:param pk:
	:return:
	"""
	obj = models.UserInfo.objects.filter(pk=pk).first()
	if not obj:
		return HttpResponse("角色不存在")

	if request.method == "GET":
		form = UpdateUserModelForm(instance=obj)  # 传到页面的时候，会自带查到的值
		return render(request, 'rbac/change.html', {'form':form})

	form = UpdateUserModelForm(instance=obj,data=request.POST)
	if form.is_valid():
		form.save()
		return redirect(reverse('rbac:user_list'))
	return render(request, 'rbac/change.html', {'form':form})


def user_reset(request,pk):
	"""
	充值密码
	:param request:
	:param pk:
	:return:
	"""
	obj = models.UserInfo.objects.filter(pk=pk).first()
	if not obj:
		return HttpResponse("角色不存在")

	if request.method == "GET":
		form = ResetUserModelForm()  # 传到页面的时候，会自带查到的值
		return render(request, 'rbac/change.html', {'form':form})

	form = ResetUserModelForm(instance=obj,data=request.POST)
	if form.is_valid():
		form.save()
		return redirect(reverse('rbac:user_list'))
	return render(request, 'rbac/change.html', {'form':form})



def user_del(request,pk):
	"""
	删除角色
	:param request:
	:param pk:
	:return:
	"""
	origin_url = reverse('rbac:user_list')

	if request.method == "GET":
		info = models.UserInfo.objects.filter(pk=pk).first()
		return render(request,'rbac/delete.html',{'info':info,"cancel":origin_url})

	models.UserInfo.objects.filter(pk=pk).delete()
	return redirect(origin_url)





