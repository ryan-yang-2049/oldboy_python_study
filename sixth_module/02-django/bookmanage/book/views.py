from django.shortcuts import render,HttpResponse,redirect
from book.models import *

def add_book(request):
	if request.method == "POST":
		title = request.POST.get("title")
		price = request.POST.get("price")
		pub_date = request.POST.get("pub_date")
		publish_id = request.POST.get("publish_id")
		author_id_list = request.POST.getlist("author_id_list") #针对多个值，checkbok 标签
		book_obj = Book.objects.create(title=title,price=price,publishDate=pub_date,publish_id=publish_id,)
		# 多对多绑定
		book_obj.authors.add(*author_id_list)
		return redirect("/books/")
	publish_list = Publish.objects.all()
	author_list = Author.objects.all()
	return render(request,"addbook.html",locals())

def books(request):
	book_list = Book.objects.all()
	return render(request,'book.html',locals())


def change_book(request,edit_book_id):
	edit_book_obj = Book.objects.filter(pk=edit_book_id).first()
	if request.method == "POST":
		title = request.POST.get("title")
		price = request.POST.get("price")
		pub_date = request.POST.get("pub_date")
		publish_id = request.POST.get("publish_id")
		author_id_list = request.POST.getlist("author_id_list")
		Book.objects.filter(pk=edit_book_id).update(title=title,price=price,publishDate=pub_date,publish_id=publish_id)
		# edit_book_obj.authors.clear()
		# edit_book_obj.authors.add(*author_id_list)
		# set 先清空，在设置。
		edit_book_obj.authors.set(author_id_list)
		return  redirect("/books/")
	publish_list = Publish.objects.all()
	author_list = Author.objects.all()
	return render(request,"editbook.html",locals())

def delete_book(request,delete_book_id):
	Book.objects.filter(pk=delete_book_id).delete()
	return redirect("/books/")
