from django.shortcuts import render,HttpResponse,redirect

# Create your views here.


from managebook.models import Book

def addbook(request):

	if request.method == "POST":
		title = request.POST.get("title")
		price = request.POST.get("price")
		publish = request.POST.get("publish")
		pub_date = request.POST.get("pub_date")

		book_obj =Book.objects.create(title=title,price=price,pub_date=pub_date,publish=publish)
		return redirect('/books/')
	return render(request,"addbook.html")


def books(request):

	book_list = Book.objects.all()

	return render(request,"books.html",locals())
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
