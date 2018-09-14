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