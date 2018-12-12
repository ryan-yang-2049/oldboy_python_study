# -*- coding: utf-8 -*-

from django.shortcuts import  HttpResponse,render,redirect
from django.urls import reverse
from cmdb import models
from rbac.service.init_permission import init_permission


def login(request):
	if request.method == "GET":
		return render(request,'cmdb/login.html')

	user = request.POST.get('username')
	pwd = request.POST.get('password')
	user_object = models.UserInfo.objects.filter(name=user,password=pwd).first()
	if not user_object:
		return render(request,'cmdb/login.html',{'error':'用户名或密码错误'})

	# 用户权限初始化
	init_permission(user_object,request)


	return redirect(reverse("cmdb:index"))

def logout(request):
	"""
	注销
	:param request:
	:return:
	"""
	request.session.delete()
	return redirect(reverse("login"))


def index(request):
	"""
	首页
	:param request:
	:return:
	"""

	return render(request,'cmdb/index.html')











