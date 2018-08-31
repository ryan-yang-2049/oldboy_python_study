# -*- coding: utf-8 -*-

# __title__ = 'classes.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.08.30'

from django.shortcuts import render,HttpResponse,redirect
from app01 import models

def get_classes(request):
	cls_list = models.Classes.objects.all()


	return render(request,"classes.html",locals())

def add_classes(request):

	if request.method == "POST":
		title = request.POST.get("title")
		models.Classes.objects.create(name=title)

		return redirect('/classes.html')



	return render(request,"add_classes.html")


def del_classes(request):
	nid = request.GET.get('nid')

	models.Classes.objects.filter(id=nid).delete()

	return redirect('/classes.html')

def edit_classes(request):
	if request.method == "GET":

		nid = request.GET.get("nid")
		obj = models.Classes.objects.filter(id=nid).first()
	elif request.method == "POST":
		nid = request.GET.get("nid")
		name = request.POST.get("name1")
		models.Classes.objects.filter(id=nid).update(name=name)
		return redirect('/classes.html')



	return render(request, 'edit_classes.html',locals())


