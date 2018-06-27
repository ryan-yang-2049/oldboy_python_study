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
	# print(book_obj.price)
	# print(book_obj.publish)  #Publish object (1)  与这本书关联的的出版社对象
	# 可以通过 book_obj.publish.email 等字段去获取对应的值


	# 查询java的出版社的邮箱
	# book_obj = Book.objects.filter(title="java").first()
	# # print(book_obj)
	# print(book_obj.publish.email)  # 123qq.com

	###########################绑定多对多的关系##################################
	book_obj = Book.objects.create(title="HTML", price=80, publishDate="2013-02-21", publish_id=1,)












	return HttpResponse("ok")