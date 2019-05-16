# -*- coding: utf-8 -*-
from django.shortcuts import render,HttpResponse,redirect
from django.urls import reverse

from app01 import models
from app01.forms.user import UserModelForm,UpdateUserModelForm,ResetPasswordUserModelForm
from rbac.service.parse_urls import memory_reverse
def user_list(request):
	"""
	用户列表
	:param request:
	:return:
	"""
	users = models.UserInfo.objects.all()
	return render(request,'rbac/user_list.html',{'users':users})


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
		return redirect(memory_reverse(request,'user_list'))
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
		return redirect(memory_reverse(request,'user_list'))
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
		form = ResetPasswordUserModelForm()  # 传到页面的时候，会自带查到的值
		return render(request, 'rbac/change.html', {'form':form})

	form = ResetPasswordUserModelForm(instance=obj,data=request.POST)
	if form.is_valid():
		form.save()
		return redirect(memory_reverse(request,'user_list'))
	return render(request, 'rbac/change.html', {'form':form})



def user_del(request,pk):
	"""
	删除角色
	:param request:
	:param pk:
	:return:
	"""
	origin_url = memory_reverse(request,'user_list')

	if request.method == "GET":
		info = models.UserInfo.objects.filter(pk=pk).first()
		return render(request,'rbac/delete.html',{'info':info,"cancel":origin_url})

	models.UserInfo.objects.filter(pk=pk).delete()
	return redirect(origin_url)
