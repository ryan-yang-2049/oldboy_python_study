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


def query_data(request):
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

	author_obj = Author.objects.filter(name="ryan").first()
	detail_obj = author_obj.authordetail.telephone
	# print(author_obj.authordetail)
	for detail in detail_obj:
		print(detail.telephone)

	return HttpResponse("query data")


'''

A与B有关系：关联属性在A表中
	正向查询： A表 -----正向查询-------> B表
	反向查询： B表 -----反向查询------->A表

一对多查询的正反向查询：
	正向查询：按字段 ==>   model对象.字段
 	反向查询：表名小写_set.all()   ==> model对象.表名小写_set.all() 

多对多查询的正反向查询
	正向查询：按字段 ==>   model对象.字段
	反向查询：表名小写_set.all()  ==> model对象.表名小写_set.all() 

一对一查询的正反向查询
	正向查询：按字段
	反向查询：按表名小写



'''