

from django.shortcuts import HttpResponse,render,redirect

from rbac import models
from rbac.service.init_permission import init_permission

'''
用户登陆相关
找模板顺序 --> 先从最外层找templates --> 从app的注册顺序找 templates目录，

'''


def login(request):

	if request.method == "GET":
		return render(request,'login.html')

	user = request.POST.get('user')
	pwd = request.POST.get('pwd')

	current_user = models.UserInfo.objects.filter(name=user,password=pwd).first()
	if not current_user:
		return render(request,'login.html',{'msg':'用户或密码错误'})

	# 用户权限初始化 rbac/service/init_permission/init_permission.py
	init_permission(current_user,request)


	return redirect('/customer/list/')





















