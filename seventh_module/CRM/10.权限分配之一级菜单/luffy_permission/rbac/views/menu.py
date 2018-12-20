# -*- coding: utf-8 -*-

# __title__ = 'menu.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.12.04'


from django.shortcuts import render,redirect,HttpResponse
from django.urls import reverse
from rbac import  models
from rbac.forms.menu import MenuModelForm
from rbac.service.parse_urls import memory_reverse_url


def menu_list(request):
	"""
	菜单列表
	:param request:
	:return:
	"""
	menus = models.Menu.objects.all()

	menu_id = request.GET.get('mid')
	print("menu_id",menu_id)

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

# 30:04