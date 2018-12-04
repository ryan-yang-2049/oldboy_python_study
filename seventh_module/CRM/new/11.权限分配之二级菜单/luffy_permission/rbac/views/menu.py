# -*- coding: utf-8 -*-

# __title__ = 'menu.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.12.04'


from django.shortcuts import render,redirect,HttpResponse
from django.urls import reverse
from rbac import  models
from rbac.forms.menu import MenuModelForm,SecondMenuModelForm,PermissionModelForm
from rbac.service.parse_urls import memory_reverse_url


def menu_list(request):
	"""
	菜单列表
	:param request:
	:return:
	"""
	# 菜单信息
	menus = models.Menu.objects.all()
	menu_id = request.GET.get('mid')    # 用户选择的一级菜单
	second_menu_id = request.GET.get('sid')    # 用户选择的二级菜单

	# 如果一级菜单的mid不存在那么久不在二级菜单里面展示"新增"按钮
	menu_exists = models.Menu.objects.filter(id=menu_id).exists()
	if not menu_exists:
		menu_id = None
	if  menu_id:
		second_menus = models.Permission.objects.filter(menu_id=menu_id)
	else:
		second_menus = []

	# 如果二级菜单的sid不存在那么久不在权限信息里面展示"新增"按钮
	second_menu_exists = models.Permission.objects.filter(id=second_menu_id).exists()
	# second_menu_exists = models.Permission.objects.filter(id=second_menu_id).values("menu__id").first()
	print("second_menu_exists",second_menu_exists,type(second_menu_exists))
	if not second_menu_exists:
		second_menu_id = None
	if second_menu_id:
		permissions = models.Permission.objects.filter(pid_id=second_menu_id)
	else:
		permissions = []


	permission_exists = models.Permission.objects.filter(id=second_menu_id).exists()
	print('permission_exists',permission_exists)
	if permission_exists:
		second_menu_exists = models.Permission.objects.filter(id=second_menu_id).values("menu__id").first()
		print("second_menu_exists",second_menu_exists,type(second_menu_exists))
		if not second_menu_exists["menu__id"]:
			second_menu_id = None
		if second_menu_id:
			permissions = models.Permission.objects.filter(pid_id=second_menu_id)
		else:
			permissions = []
	else:
		permissions = []

	return render(request,'rbac/menu_list.html',locals())

# 15:40
def menu_add(request):
	"""

	:param request:
	:return:
	"""

	if request.method == "GET":
		form = MenuModelForm()
		return render(request, 'rbac/change.html', {'form':form})

	form = MenuModelForm(data=request.POST)
	if form.is_valid():
		form.save()
		return redirect(memory_reverse_url(request,'rbac:menu_list'))

	return render(request, 'rbac/change.html', {'form': form}) # 如果输入为空，则在form 中有errors的错误信息

def menu_edit(request,pk):
	obj = models.Menu.objects.filter(id=pk).first()
	if not obj:
		return HttpResponse("菜单不存在")


	if request.method == "GET":
		form = MenuModelForm(instance=obj)

		return render(request, 'rbac/change.html', {"form":form})

	form = MenuModelForm(instance=obj,data=request.POST)
	if form.is_valid():
		form.save()
		return redirect(memory_reverse_url(request, 'rbac:menu_list'))

	return render(request, 'rbac/change.html', {"form": form})


def menu_del(request,pk):
	# 用户点击取消删除角色按钮以后就回到role_list 界面
	origin_url = memory_reverse_url(request,'rbac:menu_list')

	if request.method == "GET":

		return render(request, 'rbac/delete.html', {"cancel":origin_url})

	models.Menu.objects.filter(id=pk).delete()
	return redirect(origin_url)



def second_menu_add(request,menu_id):
	"""
	添加二级菜单
	:param request:
	:param menu_id: 已选择的一级菜单ID(用于设置默认值)
	:return:
	"""

	menu_obj = models.Menu.objects.filter(pk=menu_id).first()
	if request.method == "GET":
		form = SecondMenuModelForm(initial={'menu':menu_obj})
		return render(request, 'rbac/change.html', {'form':form})

	form = SecondMenuModelForm(data=request.POST)
	if form.is_valid():
		form.save()
		return redirect(memory_reverse_url(request,'rbac:menu_list'))

	return render(request, 'rbac/change.html', {'form': form})


def second_menu_edit(request,pk):
	"""
	编辑二级菜单
	:param request:
	:param pk:
	:return:
	"""
	obj = models.Permission.objects.filter(id=pk).first()
	if not obj:
		return HttpResponse("菜单不存在")


	if request.method == "GET":
		form = SecondMenuModelForm(instance=obj)

		return render(request, 'rbac/change.html', {"form":form})

	form = SecondMenuModelForm(instance=obj,data=request.POST)
	if form.is_valid():
		form.save()
		return redirect(memory_reverse_url(request, 'rbac:menu_list'))
	return render(request, 'rbac/change.html', {"form": form})


def second_menu_del(request,pk):
	"""
	删除二级菜单
	:param request:
	:param pk:
	:return:
	"""
	# 用户点击取消删除角色按钮以后就回到role_list 界面
	origin_url = memory_reverse_url(request,'rbac:menu_list')

	if request.method == "GET":

		return render(request, 'rbac/delete.html', {"cancel":origin_url})

	models.Permission.objects.filter(id=pk).delete()
	return redirect(origin_url)


def permission_add(request,second_menu_id):
	"""
	增加权限信息
	:param request:
	:param second_menu_id: 关联的父级菜单ID
	:return:
	"""
	if request.method == "GET":
		form = PermissionModelForm()
		return render(request, 'rbac/change.html', {'form':form})

	form = PermissionModelForm(data=request.POST)
	if form.is_valid():
		second_menu_object = models.Permission.objects.filter(id=second_menu_id).first()
		if not  second_menu_object:
			return HttpResponse("二级菜单不存在，请重新选择！")
		# form.instance 中包含了用户提交的所有值
		#
		form.instance.pid = second_menu_object

		form.save()
		return redirect(memory_reverse_url(request,'rbac:menu_list'))

	return render(request, 'rbac/change.html', {'form': form})




