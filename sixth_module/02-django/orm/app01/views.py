from django.shortcuts import render,HttpResponse

# Create your views here.


from app01.models import Book

def index(request):

	#添加表记录

	# 方式一：
	book_obj1 = Book(id=1,title="python红宝书",price=100,pub_date="2012-12-12",publish="人民出版社")
	book_obj1.save()

	#方式二：create返回值就是当前生成的对象记录

	book_obj2 = Book.objects.create(title="java",price=200,pub_date="2013-01-13",publish="人民出版社")

	print(book_obj2.title)
	print(book_obj2.price)
	print(book_obj2.publish)

	return HttpResponse("OK")