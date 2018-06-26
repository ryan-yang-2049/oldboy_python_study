from django.shortcuts import render,HttpResponse

# Create your views here.


from app01.models import Book


def insert(request):
	# ========================================添加表记录========================================

	# # 方式一：
	# book_obj1 = Book(id=1,title="python红宝书",price=100,pub_date="2012-12-12",publish="人民出版社")
	# book_obj1.save()
	#
	# #方式二：create返回值就是当前生成的对象记录
	#
	book_obj1 = Book.objects.create(title="python红宝书", price=100, pub_date="2012-12-12", publish="人民出版社")
	book_obj2 = Book.objects.create(title="php", price=150, pub_date="2012-09-13", publish="人民出版社")
	book_obj3 = Book.objects.create(title="go", price=100, pub_date="2018-06-21", publish="上海出版社")
	book_obj4 = Book.objects.create(title="java", price=200, pub_date="2013-01-13", publish="人民出版社")
	book_obj5 = Book.objects.create(title="go", price=180, pub_date="2018-06-14", publish="南京出版社")
	book_obj6 = Book.objects.create(title="python2.7", price=100, pub_date="2012-12-12", publish="人民出版社")
	book_obj7 = Book.objects.create(title="python3", price=150, pub_date="2018-09-12", publish="人民出版社")
	#
	# print(book_obj2.title)
	# print(book_obj2.price)
	# print(book_obj2.publish)
	return HttpResponse("OK")

def index(request):


	# ========================================查询表记录API========================================
	'''
	1.方法的返回值
	2.方法的调用者
	:param request:
	:return:
	'''
	# (1) all方法 ： 返回一个 QuerySet 对象
	# QuerySet 类似一个列表放了一个个 object对象
	# book_list = Book.objects.all()
	# print(book_list)
	# # 结果：<QuerySet [<Book: python红宝书>, <Book: php>, <Book: go>, <Book: java>, <Book: go>, <Book: python2.7>, <Book: python3>]>
	# for obj in book_list:
	# 	print(obj.title,obj.price)
	#
	# print(book_list[1].title,book_list[1].price)   #php 150.00

	# (2) first，last 方法 : 调用者：queryset对象，返回值：model对象
	print(Book.objects.all().first())  # 结果：python红宝书  。相当于 Book.objects.all()[0]
	print(Book.objects.all().last()) # 结果：python3

	# (3) filter()  返回值：queryset对象
	# print(Book.objects.filter(title='php'))
	# print(Book.objects.filter(price=100))  #<QuerySet [<Book: python红宝书>, <Book: go>]>
	#
	# book_obj = Book.objects.filter(price=100).first()
	# print(book_obj)   # python红宝书
	# print(Book.objects.filter(title='go',price=150))   # 过滤多个条件

	# (4) get() 有且只有一个查询结果时才有意义 返回值：model对象
	# 没有返回值报错，超过一个查询结果也报错。
	# book_obj = Book.objects.get(title='go')
	# print(book_obj.price)

	# (5)exclude  排除  返回值：queryset对象
	# print(Book.objects.exclude(title='go'))

	# (6)order_by 排序 ,调用者：queryset对象 ,返回值：QuerySet 对象    降序 在字段前面加 “-”
	# ret = Book.objects.all().order_by("-id")  #按照 ID 降序排列
	# ret = Book.objects.all().order_by("-price")  # 价格排序
	# ret = Book.objects.all().order_by("price","id")  # 按照价格,id排序，(先排序价格，如果相同，在排序ID)
	# print(ret)

	# (7) reverse   对查询结果反向排序

	# (8) count 返回数据库中匹配查询(QuerySet)的对象数量。调用者：queryset对象，返回值：int
	# ret = Book.objects.all().count()
	# print(ret)

	# (9) exists() 如果QuerySet包含数据，就返回True，否则返回False
	# ret = Book.objects.exclude(title='go').exists()
	# ret = Book.objects.all().exists()
	# print(ret)

	# (10) values 方法(很重要):返回一个ValueQuerySet——一个特殊的QuerySet，运行后得到的并不是一系列model的实例化对象，而是一个可迭代的字典序列
	# 调用对象：queryset对象 ； 返回值：queryset对象
	# '''
	# values：工作原理
	# temp = []
	# for obj in Book.objects.all():
	# 	temp.append({
	# 		"price"=obj.price
	#       "title"=obj.title
	# 	})
	# return temp
	# '''
	# ret = Book.objects.all().values("price","title")
	# # <QuerySet [{'price': Decimal('100.00'), 'title': 'python红宝书'}, {'price': Decimal('150.00'), 'title': 'php'}, {'price': Decimal('200.00'), 'title': 'java'}, {'price': Decimal('100.00'), 'title': 'go'}, {'price': Decimal('180.00'), 'title': 'go'}]>
	#
	# print(ret[1].get('price'))


	# (11) values_list(*field):   它与values()非常相似，它返回的是一个元组序列，values返回的是一个字典序列
	# ret = Book.objects.all().values_list("price","title")
	# <QuerySet [(Decimal('100.00'), 'python红宝书'), (Decimal('150.00'), 'php'), (Decimal('200.00'), 'java'), (Decimal('100.00'), 'go'), (Decimal('180.00'), 'go')]>
	# print(ret)

	# (12) distinct  从返回结果中剔除重复纪录
	#
	# ret = Book.objects.all().values('price').distinct()
	# print(ret)

	# ========================================查询表记录--模糊查询========================================
	# 大于100 小于200
	# ret = Book.objects.filter(price__gt=100,price__lt=200)    # <QuerySet [<Book: php>, <Book: go>]>
	# print(ret)

	# 以什么什么开头/结尾的书籍
	# ret = Book.objects.filter(title__startswith='py') # <QuerySet [<Book: python红宝书>]>
	# ret2 = Book.objects.filter(title__endswith='va')   # <QuerySet [<Book: java>]>
	# print(ret)

	# 包含什么什么的书籍  (title__icontains 不区分大小写)
	# print(Book.objects.filter(title__contains='o'))  #<QuerySet [<Book: python红宝书>, <Book: go>, <Book: go>]>

	# in 在列表里面的值
	# print(Book.objects.filter(price__in=[100,200])) #<QuerySet [<Book: python红宝书>, <Book: java>, <Book: go>]>

	# 在什么什么区间范围
	# print(Book.objects.filter(price__range=[150,180]))

	# 查询年份,月份
	# print(Book.objects.filter(pub_date__year=2012,pub_date__month=12))   #<QuerySet [<Book: python红宝书>]>


	# ========================================单表 删除记录和修改记录========================================
	# delete： 调用者：queryset对象  model对象
	# delete调用queryset对象
	# ret = Book.objects.filter(price__range=[100,200]).delete()
	# print(ret)
	# delete调用model对象
	# Book.objects.filter(price=100).first().delete()

	# 更新/修改  update ， update只能是queryset 去调用
	# Book.objects.filter(title="go",price=180).update(title="JavaScript")

	return HttpResponse("OK")

def query(request):
	# 查询老男孩出版社出版过的价格大于200的书籍
	# ret =Book.objects.filter(publish="老男孩出版社",price__gt=200)

	# 查询2017年8月出版的所有以py开头的书籍名称
	# ret = Book.objects.filter(title__startswith='py',pub_date__year=2017,pub_date__month=8).values("title")

	# 查询价格为50, 100 或者150的所有书籍名称及其出版社名称
	# Book.objects.filter(price__in=[50,100,150]).values("title","publish")

	# 查询价格在100到200之间的所有书籍名称及其价格
	# Book.objects.filter(price__range=[100,200]).values("title","price")

	# 查询所有人民出版社出版的书籍的价格（从高到低排序，去重）
	# Book.objects.filter(publish="人民出版社").values("price").distinct().order_by("-price")


	return HttpResponse("OK")














