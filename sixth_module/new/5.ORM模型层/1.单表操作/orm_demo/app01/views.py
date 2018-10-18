from django.shortcuts import render,HttpResponse

from app01.models import Book

# 添加表记录
def index_insert(request):
	# 添加表记录
	# 方式1：  obj.save()
	# book_obj1 = Book(id=1, title="python红宝书", price=100, pub_date="2012-12-12", publish="人民出版社")
	# book_obj1.save()

	# 方式2：
	# book_obj = Book.objects.create(title="php", price=100, pub_date="2013-12-12", publish="人民出版社")
	# book_obj = Book.objects.create(title="go", price=120, pub_date="2016-08-12", publish="南京出版社")
	# print("book_obj.title===>:",book_obj.title)
	# print("book_obj.price===>:",book_obj.price)
	# print("book_obj.pub_date===>:",book_obj.pub_date)
	return HttpResponse("OK insert")

# 查询表记录
def index(request):
	'''
		1.方法的返回值
		2.方法的调用者
	:param request:
	:return:
	'''
	# (1) all方法：返回一个queryset对象
	# book_res = Book.objects.all()
	# print(book_res) # <QuerySet [<Book: python红宝书>, <Book: php>]>
	#
	# for obj in book_res:    # 此时的obj是每一本书的对象
	# 	print(obj.title,obj.price,obj.pub_date)


	# (2) first,last : 调用者：queryset对象 ,返回值：model对象(Book模型下的对象)
	# book_first = Book.objects.all().first()
	# book_first = Book.objects.all()[0]
	# print(book_first)
	# print(type(book_first))


	# (3)filter()
	# book_filter = Book.objects.filter(price=100)
	# print(book_filter)
	# print(book_filter.first())

	# (4) get() :有且只有一个查询结果时才有意义
	# book_obj = Book.objects.get(title='go')
	# print(book_obj.price)

	# (5) exclude : 除了什么之外
	# book_obj = Book.objects.exclude(title="go")
	# print(book_obj)

	# (6) order_by : 排序
	# book_obj = Book.objects.all().order_by('-price','-id')
	# print(book_obj)

	# (7) count()计数
	# (8) exist()
	# ret = Book.objects.all().exists()
	# if ret:
	# 	print(True)

	# (9) values:  调用者：queryset ,返回值:queryset
	# ret = Book.objects.all().values('title','price')
	# print(ret)
	# print(ret[0].get('price))


	# (10) values_list 方法
	ret = Book.objects.values_list('title','price')
	print(ret)

	return HttpResponse("OK")
















