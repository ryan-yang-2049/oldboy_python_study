from django.shortcuts import render,redirect
# Create your views here.
from app01.models import  Book
# 书籍首页
def books(request):
	book_list = Book.objects.all()
	return render(request,"books.html",locals())
# 添加书籍页面
def addbook(request):
	if request.method == "POST":
		titile = request.POST.get("title")
		price = request.POST.get("price")
		date = request.POST.get("date")
		publish = request.POST.get("publish")
		# 书籍信息插入到数据库
		Book.objects.create(title=titile,price=price,pub_date=date,publish=publish)
		return redirect("/books/")
	return render(request,"addbook.html")
# 删除书籍信息
def delbook(request,id):
	Book.objects.filter(id=id).delete()
	return redirect("/books/")
# 修改书籍信息
def changebook(request,id):
	book_obj = Book.objects.filter(id=id).first()
	if request.method == "POST":
		titile = request.POST.get("title")
		price = request.POST.get("price")
		date = request.POST.get("date")
		publish = request.POST.get("publish")
		# 更新数据库书籍信息
		Book.objects.filter(id=id).update(title=titile,price=price,pub_date=date,publish=publish)
		return redirect('/books/')
	return render(request,"changebook.html",locals())



# a标签默认是get请求








