from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
from app01.models import  Book

def addbook(request):

	if request.method == "POST":
		titile = request.POST.get("title")
		price = request.POST.get("price")
		date = request.POST.get("date")
		publish = request.POST.get("publish")
		book_obj=Book.objects.create(title=titile,price=price,pub_date=date,publish=publish)

		return redirect("/books/")
	return render(request,"addbook.html")



def books(request):

	book_list = Book.objects.all()



	return render(request,"books.html",locals())


def delbook(request,id):

	Book.objects.filter(id=id).delete()

	return redirect("/books/")


def changebook(request,id):

	book_obj = Book.objects.filter(id=id).first()
	if request.method == "POST":
		titile = request.POST.get("title")
		price = request.POST.get("price")
		date = request.POST.get("date")
		publish = request.POST.get("publish")
		# book_obj=Book.objects.create(title=titile,price=price,pub_date=date,publish=publish)
		Book.objects.filter(id=id).update(title=titile,price=price,pub_date=date,publish=publish)

		return redirect('/books/')


	return render(request,"changebook.html",locals())



# a标签默认是get请求








