from django.shortcuts import render,HttpResponse

# Create your views here.
from app01.models import *

def add(request):
	# Publish.objects.create(name="人民出版社",email="123qq.com",city="beijing")
	# Publish.objects.create(name="新华出版社",email="1234qq.com",city="beijing")

	########################绑定一对多的关系######################################
	# 方式一
	# 为book表绑定出版社：publish
	# 为方式二理解下：就算赋值了 publish_id=1 也会有一个 publish的对象
	# book_obj = Book.objects.create(title="python",price=100,publishDate="2012-12-11",publish_id=1)
	# print(book_obj.title,book_obj.publish_id)

	# 方式二 publish等于一个实例模型对象
	# pub_obj = Publish.objects.filter(nid=2).first()
	# book_obj = Book.objects.create(title="JavaScript",price=180,publishDate="2017-08-14",publish=pub_obj)
	# print(book_obj.title)
	# print(book_obj.publish)  #Publish object (1)  与这本书关联的的出版社对象
	# print(book_obj.publish.email)
	# 可以通过 book_obj.publish.email 等字段去获取对应的值


	# 查询java的出版社的邮箱
	# book_obj = Book.objects.filter(title="java").first()
	# print(book_obj.publish.email)  # 123qq.com

	###########################绑定多对多的关系##################################
	# 此时多对多的关系生成的那张表在名称空间里面没有（models.py）。不能直接用objects去操作表。因此，django提供了一个接口去操作多对多的那张表
	# book_obj = Book.objects.create(title="HTML", price=80, publishDate="2013-02-21", publish_id=1)
	#
	# ryan = Author.objects.get(name="ryan")
	# cherry = Author.objects.get(name="cherry")
	#
	# # 绑定多对多关系的API
	# book_obj.authors.add(ryan,cherry)
	# # book_obj.authors.add(1,2) # 此时的1和2 就是ryan和cherry对应的主键ID
	# # book_obj.authors.add(1,2)  等价于  book_obj.authors.add(*[1,2])



	# 解除多对多关系
	book = Book.objects.filter(nid=4).first()
	# book.authors.remove(1) # 删除 nid=4 的书籍在 book_authors中作者ID等于1的关系。
	# # book.authors.remove(1，2) 等价于book.authors.remove(*[1,2])
	# #
	# book.authors.clear() #清空所有book 的nid=4 对象的关系主键

	print(book.authors.all()) # 返回 <QuerySet [<Author: cherry>]> ;  获取与这本书关联的所有作者对象集合

	print(book.authors.all().values("name")) # <QuerySet [{'name': 'cherry'}]>
	print(book.authors.all().values("name")[0].get("name")) # cherry





	return HttpResponse("ok")