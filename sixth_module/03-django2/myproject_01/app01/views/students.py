# -*- coding: utf-8 -*-

# __title__ = 'students.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.08.30'

from django.shortcuts import render,redirect,HttpResponse
from app01 import models

def get_students(request):
	stu_list = models.Student.objects.all()

	return render(request,"students.html",locals())


def add_students(request):

	cs_list = models.Classes.objects.all()

	if request.method == "POST":
		username = request.POST.get("username")
		age = request.POST.get("age")
		gender = request.POST.get("gender")

		cs = request.POST.get("cs")


		models.Student.objects.create(username=username,age=age,gender=gender,cs_id=cs)

		return redirect("/students.html")

	return render(request,'add_students.html',locals())


def del_student(request):
	nid = request.GET.get("nid")

	models.Student.objects.filter(id=nid).delete()

	return redirect("/students.html")


def edit_student(request):
	nid = request.GET.get("nid")
	cs_list = models.Classes.objects.all()
	stu_obj = models.Student.objects.filter(id=nid).first()

	if request.method == "POST":
		nid = request.GET.get("nid")
		username = request.POST.get("username")
		age = request.POST.get("age")
		gender = request.POST.get("gender")
		cs = request.POST.get("cs")
		models.Student.objects.filter(id=nid).update(username=username,age=age,gender=gender,cs_id=cs)
		return  redirect("/students.html")

	return render(request,"edit_students.html",locals())
