# -*- coding: utf-8 -*-

from django.shortcuts import HttpResponse, render, redirect
from django.urls import reverse
from rbac.service.routes import get_all_url_dict
from rbac.forms.menuform import MenuModelForm,SecondMenuModelForm,PermissionModelForm
from rbac import models
from rbac.service.parse_urls import memory_reverse


def menu_list(request):
	"""
	菜单展示
	:param request:
	:return:
	"""
	menu_queryset = models.Menu.objects.all()
	menu_id = request.GET.get('mid')    # 选择的一级菜单
	second_menu_id = request.GET.get('sid')    # 选择的一级菜单

	menu_exists = models.Menu.objects.filter(id=menu_id).exists()
	if not menu_exists:
		menu_id = None
	if menu_id:
		second_menus = models.Permission.objects.filter(menu_id = menu_id)
	else:
		second_menus = []

	permission_exists = models.Permission.objects.filter(id=second_menu_id).values("menu_id")
	if permission_exists:
		second_menu_exists = models.Permission.objects.filter(id=second_menu_id).values("menu__id").first()
		if not second_menu_exists["menu__id"]:
			second_menu_id = None
		if second_menu_id:
			permissions = models.Permission.objects.filter(pid_id=second_menu_id)
		else:
			permissions = []
	else:
		permissions = []

	return render(
		request,
		'rbac/menu_list.html',
		{
			"menus": menu_queryset,
			"menu_id": menu_id,
			"second_menu_id": second_menu_id,
			"second_menus": second_menus,
			"permissions":permissions
		})


def menu_add(request):
	"""
	添加角色
	:param request:
	:return:
	"""
	if request.method == "GET":
		form = MenuModelForm()
		return render(request, 'rbac/change.html', {'form': form})
	form = MenuModelForm(request.POST)
	if form.is_valid():
		form.save()
		return redirect(memory_reverse(request, "rbac:menu_list"))
	return render(request, 'rbac/change.html', {'form': form})


def menu_edit(request, pk):
	"""
	编辑一级菜单
	:param request:
	:param pk:
	:return:
	"""
	obj = models.Menu.objects.filter(pk=pk).first()
	if not obj: return HttpResponse("菜单不存在")

	if request.method == "GET":
		form = MenuModelForm(instance=obj)  # 传到页面的时候，会自带查到的值
		return render(request, 'rbac/change.html', {'form': form})

	form = MenuModelForm(instance=obj, data=request.POST)
	if form.is_valid():
		form.save()
		return redirect(memory_reverse(request, "rbac:menu_list"))
	return render(request, 'rbac/change.html', {'form': form})


def menu_del(request, pk):
	"""
	删除一级菜单
	:param request:
	:param pk:
	:return:
	"""
	origin_url = memory_reverse(request, "rbac:menu_list")

	if request.method == "GET":
		info = models.Menu.objects.filter(pk=pk).first()
		return render(request, 'rbac/delete.html', {'info': info, "cancel": origin_url})

	models.Menu.objects.filter(pk=pk).delete()
	return redirect(origin_url)

def second_menu_add(request,menu_id):
	"""
	添加二级菜单
	:param request:
	:param menu_id: 已选择的一级菜单ID，(用于设置默认值)
	:return:
	"""
	menu_obj = models.Menu.objects.filter(id=menu_id).first()

	if request.method == "GET":
		form = SecondMenuModelForm(initial={'menu':menu_id})    # 返回页面时的默认值
		return render(request, 'rbac/change.html', {'form': form})
	form = SecondMenuModelForm(request.POST)
	if form.is_valid():
		form.save()
		return redirect(memory_reverse(request, "rbac:menu_list"))
	return render(request, 'rbac/change.html', {'form': form})

def second_menu_edit(request, pk):
	"""
	编辑二级菜单
	:param request:
	:param pk: 当前要编辑的二级菜单
	:return:
	"""
	permission_obj = models.Permission.objects.filter(pk=pk).first()

	if request.method == "GET":
		form = SecondMenuModelForm(instance=permission_obj)  # 传到页面的时候，会自带查到的值，也就是页面上显示的默认值
		return render(request, 'rbac/change.html', {'form': form})

	form = SecondMenuModelForm(instance=permission_obj, data=request.POST)  # 保存的时候，要把默认值也携带上
	if form.is_valid():
		form.save()
		return redirect(memory_reverse(request, "rbac:menu_list"))
	return render(request, 'rbac/change.html', {'form': form})

def  second_menu_del(request, pk):
	"""
	删除二级菜单
	:param request:
	:param pk:
	:return:
	"""
	origin_url = memory_reverse(request, "rbac:menu_list")

	if request.method == "GET":
		info = models.Permission.objects.filter(pk=pk).first()
		return render(request, 'rbac/delete.html', {'info': info, "cancel": origin_url})

	models.Permission.objects.filter(pk=pk).delete()
	return redirect(origin_url)




def permission_add(request,second_menu_id):
	"""
	添加非菜单权限
	:param request:
	:param second_menu_id:
	:return:
	"""
	if request.method == "GET":
		form = PermissionModelForm()
		return render(request, 'rbac/change.html', {'form': form})
	form = PermissionModelForm(data=request.POST)
	if form.is_valid():
		second_menu_object  = models.Permission.objects.filter(id=second_menu_id).first()
		if not second_menu_object:
			return HttpResponse("二级菜单不存在，请重新选中")
		form.instance.pid = second_menu_object
		"""
		此时的 form.instance .pid = second_menu_object 相当于
		instance.pid = second_menu_object
		instance = models.Permission(title='',name='',url='',pid=second_menu_object)
		"""
		form.save()
		return redirect(memory_reverse(request, "rbac:menu_list"))
	return render(request, 'rbac/change.html', {'form': form})



def permission_edit(request, pk):
	"""
	编辑非菜单权限
	:param request:
	:param pk: 当前要编辑的权限ID
	:return:
	"""
	print(pk)
	permission_obj = models.Permission.objects.filter(id=pk).first()
	print(permission_obj)
	if request.method == "GET":
		form = PermissionModelForm(instance=permission_obj)  # 传到页面的时候，会自带查到的值，也就是页面上显示的默认值
		return render(request, 'rbac/change.html', {'form': form})

	form = PermissionModelForm(instance=permission_obj, data=request.POST)  # 保存的时候，要把默认值也携带上
	if form.is_valid():
		form.save()
		return redirect(memory_reverse(request, "rbac:menu_list"))
	return render(request, 'rbac/change.html', {'form': form})

def  permission_del(request, pk):
	"""
	删除非菜单权限
	:param request:
	:param pk:
	:return:
	"""
	origin_url = memory_reverse(request, "rbac:menu_list")

	if request.method == "GET":
		info = models.Permission.objects.filter(pk=pk).first()
		return render(request, 'rbac/delete.html', {'info': info, "cancel": origin_url})

	models.Permission.objects.filter(pk=pk).delete()
	return redirect(origin_url)






"""
formset 
	Form组件或ModelForm组件用于一个表单验证。
	formset用于做多个表单验证的组件
	应用场景：批量操作
	如何实现formset？
自动发现项目中的URL：
	问题：给你一个项目，请帮我获取当前项目中都有哪些URL以及name，   例如: rbac:permission_list
	实现思路:
"""




def multi_permissions(request):
	"""
	批量操作权限
	:param request:
	:return:
	"""

	# 获取项目中所有的URL
	all_url_dict = get_all_url_dict()
	for k,v in all_url_dict.items():
		print(k,v)

	return HttpResponse("ok.......")



