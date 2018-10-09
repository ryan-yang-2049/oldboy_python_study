# -*- coding: utf-8 -*-

# __title__ = 'acount.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.09.05'

from django.shortcuts import HttpResponse,render,redirect
from rbac import models


def login(request):
	
	if request.method == "GET":
		print("login")
		return render(request,"login.html")
	
	user = request.POST.get('user')
	pwd = request.POST.get('pwd')

	current_user =models.UserInfo.objects.filter(name=user,password=pwd).first()
	if not  current_user:
		return render(request,"login.html",{'msg':"用户名或者密码错误"})
	
	# 根据当前用户信息获取此用户所拥有的所有权限，并放入session
	# 当前用户的所有权限
	# queryset 对象不能直接放在session中进行实例化对象
	permissions_queryset = current_user.roles.filter(permissions__isnull=False).values("permissions__id","permissions__url").distinct()

	# 获取权限中所有的url
	permissions_list = [ item['permissions__url'] for item in permissions_queryset]

	request.session['luffy_permission_url_list_key'] = permissions_list
	return redirect('/customer/list/')

