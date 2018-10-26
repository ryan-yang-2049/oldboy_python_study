from django.shortcuts import render,HttpResponse

# Create your views here.

from app01.models import *

def add_data(request):
	# Publish.objects.create(name="人民出版社", email="123qq.com", city="beijing")
	# Publish.objects.create(name="新华出版社", email="456qq.com", city="beijing")


	################# 绑定一对多的关系 ############################
	# 方式一：
	# 为book表绑定出版社：Publish
	# book_obj = Book.objects.create(title="python", price=100, publishDate="2012-12-11", publish_id=1)
	# print(book_obj.title)

	# 方式二：
	# pub_obj = Publish.objects.filter(nid=2).first()  # model 对象
	# book_obj = Book.objects.create(title="HTML", price=80, publishDate="2012-06-14", publish=pub_obj)
	#
	# print(book_obj.title)
	# print(book_obj.publish.email) #  与这本书关联的的出版社对象
	# print(book_obj.publish_id)

	################# 绑定多对多的关系 ############################

	# book_obj = Book.objects.create(title="jQuery", price=150, publishDate="2014-08-14", publish_id=1)
	# book_obj = Book.objects.filter(title="CSS").first()
	# egon = Author.objects.get(name="egon")
	# alex = Author.objects.get(name="alex")
	# ryan = Author.objects.get(name="ryan")
	# cherry = Author.objects.get(name="cherry")

	# 绑定多对多关系的API
	# book_obj.authors.add(cherry,ryan)
	# book_obj.authors.add(2,3)
	# book_obj.authors.add(*[2,3,4])

	# 解除多对多关系的API
	book_obj = Book.objects.filter(nid=2).first()
	print(book_obj.authors.all().values('name'))

	# book_obj.authors.remove(2)
	# book_obj.authors.remove(3,4)
	# book_obj.authors.remove(*[3,4])
	# book_obj.authors.clear()    # 清空全部

	return HttpResponse("insert data")


def query(request):
	"""
	跨表查询：
		1.基于对象的查询

		2.基于双下划綫查询

		3.聚合与分组查询

		4.F与Q查询
	:param request:
	:return:
	"""

	#-------------------基于对象的跨表查询(子查询)-------------------------#
	# 一对多查询的正向查询：查询python 出版社的名字
	# book_obj =Book.objects.filter(title="python").first()
	# print(book_obj.publish)  # 与这本书关联的出版社对象
	# print(book_obj.publish.name)

	# 一对多查询的反向查询：查询人民出版社出版过的书籍名称
	# pub_obj = Publish.objects.filter(name="人民出版社").first()
	# print(pub_obj.book_set.all())


	# 多对多查询的正向查询：查询jQuery的作者
	# book_obj = Book.objects.filter(title="jQuery").first()
	# author_list = book_obj.authors.all()
	# for author in author_list:
	# 	print(author.name)

	# 多对多查询的反向查询：查询alex出版过的书籍
	# alex_obj = Author.objects.filter(name='alex').first()
	# book_list = alex_obj.book_set.all()
	# for book in book_list:
	# 	print(book.title)


	# 一对一查询的正向查询 : 查询alex的addr
	# alex = Author.objects.filter(name='alex').first()
	# print(alex)
	# print(alex.authordetail.addr)

	# 一对一查询的反向查询 : 查询手机号为119的作者的名字和年龄
	# author_obj = AuthorDetail.objects.filter(telephone=911).first()
	# print(author_obj)


	#-------------------基于双下划綫的跨表查询(join查询)-------------------------#
	# # 一对多查询的正向查询：查询python 出版社的名字
	# # 方式一
	# pub_name = Book.objects.filter(title='python').values('publish__name')
	# print(pub_name)
	#
	# # 方式二：
	# pub_name = Publish.objects.filter(book__title='python').values('name')
	# print(pub_name)

	# # 多对多查询：查询python所有作者的名字
	# # 方式一：正向查询
	# res = Book.objects.filter(title='python').values("authors__name")
	# print(res)
	# # 方式二：反向查询
	# res = Author.objects.filter(book__title='python').values("name")
	# print(res)
	#



	# 一对一查询的正向查询 : 查询alex的addr
	# res = Author.objects.filter(name='alex').values("authordetail__telephone")
	# print(res)
	#
	# res = AuthorDetail.objects.filter(author__name='alex').values('telephone','addr')
	# print(res)

	# 查询手机号以119 开头的作者出版过的所有书籍名称以及出版社名称
	#
	# res = Author.objects.filter(authordetail__telephone__contains=911).values("book__title","book__publish__name")
	# print(res)
	#
	# res = Book.objects.filter(authors__authordetail__telephone=911).values("title","publish__name")
	# print(res)


	#-------------------聚合与分组查询-------------------------#
	#-------------聚合: aggregate() : 返回值是字典 --------------#
	# 查询所有书籍的平均价格
	# from django.db.models import Avg,Max,Min,Count
	#
	# res = Book.objects.all().aggregate(Avg("price"))    #{'price__avg': 126.0}
	# res = Book.objects.all().aggregate(avg_price =Avg("price"))    #{'avg_price': 126.0}
	# res = Book.objects.all().aggregate(avg_price =Avg("price"),max_price=Max("price"))    #{'avg_price': 126.0, 'max_price': Decimal('180')}
	# print(res)

	#-------------分组查询 --------------#

	# 查找每一个出版社的名称以及出版的书籍个数
	from django.db.models import Count,Avg,Max,Min

	# ret = Publish.objects.values("name").annotate(book_count=Count("book__title"))
	# ret = Publish.objects.values("pk").annotate(book_count=Count("book__title")).values("name","book_count")
	# ret = Book.objects.values("publish__pk").annotate(c=Count("title"))
	# print(ret)


	# 查询每一个作者的名字以及出版过的书籍的最高价格
	# ret = Author.objects.values("pk").annotate(c=Max("book__price")).values("name","c")
	# print(ret)

	# 查询每本书籍的名称以及对应的作者个数
	# ret = Book.objects.values('pk').annotate(c=Count("authors__name")).values("title","c")
	# print(ret)

	# 查询每一个出版社的名称以及出版的书籍个数
	# ret = Publish.objects.values("pk").annotate(c=Count("book__title")).values("name", "email", "c")
	# print(ret)
	# ret = Publish.objects.annotate(c=Count("book__title")).values("name", "email", "c")
	# print(ret)

	# 统计每一本以HT开头的书籍的作者个数
	# ret = Book.objects.filter(title__startswith="HT").values('pk').annotate(author_count=Count("authors__name")).values("title","author_count")
	# print(ret)
	#
	#
	# # 统计不止一个作者的书籍
	# res = Book.objects.values("pk").annotate(c=Count("authors__name")).filter(c__gt=1).values("title","c")
	# print(res)


	################## F 与Q查询 ###############################
	from django.db.models import F,Q

	# 查询评论数大于阅读数
	res = Book.objects.filter(comment_num__gt=F("read_num"))
	print(res)

	# HTML书籍的价格都提升 10 块钱
	# Book.objects.filter(title="HTML").update(price=F("price")+10)
	
	ret1 = Book.objects.filter(Q(title="HTML") & Q(price=133))
	ret2 = Book.objects.filter(~Q(title="HTML") & ~Q(price=133), publish_id=1)
	ret3 = Book.objects.filter(~Q(title="HTML") | Q(price__gt=103))

	return HttpResponse("query data")


'''

A与B有关系：关联属性在A表中
	正向查询： A表 -----正向查询-------> B表
	反向查询： B表 -----反向查询------->A表

基于对象
	一对多查询的正反向查询：
		正向查询：按字段 ==>   model对象.字段
	    反向查询：表名小写_set.all()   ==> model对象.表名小写_set.all() 
	
	多对多查询的正反向查询
		正向查询：按字段 ==>   model对象.字段
		反向查询：表名小写_set.all()  ==> model对象.表名小写_set.all() 
	
	一对一查询的正反向查询
		正向查询：按字段
		反向查询：按表名小写

基于双下划綫的跨表查询(join查询)
	key:正向查询按字段,反向查询按表名小写
	


'''

