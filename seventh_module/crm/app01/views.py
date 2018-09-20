from django.shortcuts import render,HttpResponse,redirect

from django.urls import reverse

def login(request):
	url1 = reverse('rbac:xxx:n1')
	url2 = reverse('rbac:xxx:n2')
	print(url1)
	print(url2)
	return HttpResponse("rbac login")
	# return redirect(url1)



def logout(request):
	return HttpResponse("rbac logout")



def add(request):
	return HttpResponse("rbac add")


def change(request):
	return HttpResponse("rbac change")

#
# def test(request):
# 	from app01 import models
# 	list_display = ['id','title']
# 	user_queryset = models.UserInfo.objects.all()
# 	for item in user_queryset:
# 		row = []
# 		for field in list_display:
# 			row.append(getattr(item,field))
# 		print(row)
# 	return HttpResponse(".....")


def test(request):
	from app01 import models

	list_display = ['title']        # 自定义页面显示的列
	header_list = []
	for name in list_display:

		header_list.append(models.UserInfo._meta.get_field('title').verbose_name)
	print(header_list)
	user_queryset = models.UserInfo.objects.all()
	for item in user_queryset:
		row = []
		for field in list_display:
			row.append(getattr(item,field))
		print(row)
	return HttpResponse(".....")