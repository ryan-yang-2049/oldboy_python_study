# -*- coding: utf-8 -*-

# __title__ = 'menu.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.12.04'


from django.shortcuts import render,redirect,HttpResponse
from django.urls import reverse
from rbac import  models
from rbac.forms.menu import MenuModelForm,SecondMenuModelForm
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
	menu_exists = models.Menu.objects.filter(id=menu_id).exists()
	if not menu_exists:
		menu_id = None
	if  menu_id:
		second_menus = models.Permission.objects.filter(menu_id=menu_id)
	else:
		second_menus = []

	return render(request,'rbac/menu_list.html',locals())


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