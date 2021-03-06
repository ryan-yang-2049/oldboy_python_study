# -*- coding: utf-8 -*-

# __title__ = 'user.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.11.30'



from django.shortcuts import render,redirect,HttpResponse
from django.urls import reverse
from rbac import  models
from rbac.forms.user import UserModelForm,UpdateUserModelForm,ResetPasswordUserModelForm


def user_list(request):

	user_queryset = models.UserInfo.objects.all()

	return render(request,'rbac/user_list.html',{'users':user_queryset})

def user_add(request):
	if request.method == "GET":
		form = UserModelForm()
		return render(request, 'rbac/change.html', {'form':form})

	form = UserModelForm(data=request.POST)
	if form.is_valid():
		form.save()
		return redirect(reverse('rbac:user_list'))

	return render(request, 'rbac/change.html', {'form': form}) # 如果输入为空，则在form 中有errors的错误信息


def user_edit(request,pk):
	obj = models.UserInfo.objects.filter(id=pk).first()
	if not obj:
		return HttpResponse("用户不存在")


	if request.method == "GET":
		form = UpdateUserModelForm(instance=obj)
		return render(request, 'rbac/change.html', {"form":form})

	form = UpdateUserModelForm(instance=obj,data=request.POST)
	if form.is_valid():
		form.save()
		return redirect(reverse('rbac:user_list'))

	return render(request, 'rbac/change.html', {"form": form})


def user_del(request,pk):
	"""
	用户删除
	:param request:
	:param pk:
	:return:
	"""
	# 用户取消删除用户以后会到 user_list
	origin_url = reverse('rbac:user_list')
	if request.method == "GET":

		return render(request, 'rbac/delete.html', {"cancel":origin_url})

	models.UserInfo.objects.filter(id=pk).delete()
	return redirect(origin_url)


def user_reset_pwd(request,pk):
	"""
	用户重置密码
	:param request:
	:param pk:  用户主键ID
	:return:
	"""
	obj = models.UserInfo.objects.filter(id=pk).first()
	if not obj:
		return HttpResponse("用户不存在")


	if request.method == "GET":
		form = ResetPasswordUserModelForm()
		return render(request, 'rbac/change.html', {"form":form})

	form = ResetPasswordUserModelForm(instance=obj,data=request.POST)
	if form.is_valid():
		form.save()
		return redirect(reverse('rbac:user_list'))

	return render(request, 'rbac/change.html', {"form": form})







