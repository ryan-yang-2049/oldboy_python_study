# -*- coding: utf-8 -*-

from django.shortcuts import HttpResponse,render,redirect

from rbac.models import UserInfo
from rbac.service.init_permission import init_permision
def login(request):

	if request.method == "GET":
		return render(request,'login.html')

	user = request.POST.get('user')
	pwd = request.POST.get('pwd')

	current_user = UserInfo.objects.filter(name=user,password=pwd).first()
	if not current_user:
		return render(request,'login.html',{"msg":"用户名或密码错误"})

	init_permision(request,current_user)

	return redirect('/customer/list/')


