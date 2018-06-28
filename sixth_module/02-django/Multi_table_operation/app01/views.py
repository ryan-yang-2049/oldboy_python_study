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
	# book = Book.objects.filter(nid=4).first()
	# # book.authors.remove(1) # 删除 nid=4 的书籍在 book_authors中作者ID等于1的关系。
	# # # book.authors.remove(1，2) 等价于book.authors.remove(*[1,2])
	# # #
	# # book.authors.clear() #清空所有book 的nid=4 对象的关系主键
	#
	# print(book.authors.all()) # 返回 <QuerySet [<Author: cherry>]> ;  获取与这本书关联的所有作者对象集合
	#
	# print(book.authors.all().values("name")) # <QuerySet [{'name': 'cherry'}]>
	# print(book.authors.all().values("name")[0].get("name")) # cherry

	return HttpResponse("ok")


# def query(request):
# 	"""
# 	跨表查询：
# 		1.基于对象查询
# 		2.基于双下划綫查询
# 		3.聚合和分组查询
# 		4. F 与 Q 查询
# 	:param request:
# 	:return:
# 	"""
# ############################基于对象的跨表查询(子查询)###################################
#
# 	# 一对多查询的正向查询： 查询python这本书的出版社的名字
# 	# book_obj = Book.objects.filter(title="python").first()
# 	# print(book_obj.publish)
# 	# print(book_obj.publish.name)
# 	#
# 	# # 一对多查询的反向查询：查询新华出版社出版了什么书籍
# 	# publish_obj = Publish.objects.filter(name="新华出版社").first()
# 	# print(publish_obj.book_set.all())   # QuerySet
#
# 	# 多对多查询的正向查询 ：查询XHTML所有作者的名字
# 	# book_obj = Book.objects.filter(title="XHTML").first()
# 	# author_list = book_obj.authors.all()  # QuerySet 对象
# 	# for author in author_list:
# 	# 	print(author.name)
#
# 	# 多对多查询的反向查询 ：查询ryan出版过的所有书籍的名称
# 	# author_obj = Author.objects.filter(name='ryan').first()
# 	# book_list = author_obj.book_set.all()
# 	# for book in book_list:
# 	# 	print(book.title)
#
# 	# 一对一查询的正向查询：查找ryan详情
# 	# author_obj = Author.objects.filter(name="ryan").first()
# 	# print(author_obj.authordetail.telephone)
#
# 	# 一对一查询的正向查询：查询手机号为 911 的作者名
# 	# author_obj = AuthorDetail.objects.filter(telephone=911).first()
# 	# print(author_obj.author.name)
#
#
#
#
#
#
#
# """
# 基于对象的跨表查询
# A与B有关系：关联属性在A表中
# 正向查询：A ----正向查询--->B
# 反向查询：B ----反向查询--->A
#
# # 一对多查询的正反向查询
# 	正向查询: 按字段
# 	反向查询: 表名小写_set.all()
#
# 			                正向查询  book_obj.publish
# 	Book(关联属性：publish) --------------------------------------> Publish
# 						   <--------------------------------------
# 						反向查询 	publish_obj.book_set.all() #QuerySet
#
# # 多对多查询的正反向查询
# 	正向查询: 按字段
# 	反向查询: 表名小写_set.all()
#
# 			                       正向查询  book_obj.authors.all()
# 	Book(关联属性：authors)对象 --------------------------------------> Author对象
# 						       <--------------------------------------
# 						          反向查询 publish_obj.book_set.all() #QuerySet
#
# # 一对一查询的正反向查询
# 	正向查询: 按字段
# 	反向查询: 表名小写
#
# 			                                正向查询  author.authordetail
# 	Author(关联属性：authordetail对象)对象 --------------------------------------> AuthorDetail对象
# 						                 <--------------------------------------
# 						                    反向查询 authordetail.author
# """

def query(request):

	###############################基于双下划线的跨表查询(join查询)###################################
	'''
		基于双下划线的跨表查询(join查询)
		正向查询：按字段
		反向查询：按表名小写
	# 正向查询按字段，反向查询按表名小写 用来告诉ORM引擎join那张表
	'''
	# 一对多查询： 查询python这本书的出版社的名字
	# 方式一:正向
	# book_obj = Book.objects.filter(title="XHTML").values("publish__name")
	# print(book_obj)     # <QuerySet [{'publish__name': '人民出版社'}]>

	# 方式二：反向
	# ret = Publish.objects.filter(book__title="XHTML").values("name")
	# print(ret)

	# 多对多查询 ：查询XHTML书籍所有作者的名字
	# 方式一：正向
	# 需求：通过Book表join与其关联的Author表,属于正向查询：按照字段authors通知ORM引擎join book_authors 与 author
	# ret = Book.objects.filter(title="XHTML").values("authors__name")
	# for author in ret:
	# 	print(author.get('authors__name'))
	# 方式二：反向
	# 需求：通过Author表join与其关联的Book表，属于反向查询：按表名小写book通知ORM通知join book_authors 与 author表
	# ret = Author.objects.filter(book__title="XHTML").values("name")
	# print(ret)

	# 一对一查询：查找ryan详情
	# 方式一：正向
	# 需求：通过Author表join与其关联的AuthorDetail表，属于正向查询：按照字段authordetail 通知ORM引擎 join author 表 与 AuthorDetail表
	# author_obj = Author.objects.filter(name="ryan").values("authordetail__telephone")
	# print(author_obj)

	# 方式二：反向
	# 需求：通过AuthorDetail表join与其关联的Author表，属于反向查询：按表名小写author通知ORM通知join author 表 与 AuthorDetail表
	# author_obj = AuthorDetail.objects.filter(author__name="ryan").values("telephone")
	# print(author_obj)

	############################### 连续跨表 ###################################
	#进阶练习
	#练习：手机号以 110 开头的作者出版过的所有书籍名称以及书籍出版社名称

	#方式一：
	# 需求：通过Book表join AuthorDetail表，Book与AuthorDetail无关联，所以必须连续跨表
	# ret = Book.objects.filter(authors__authordetail__telephone__startswith="110").values("title","publish__name")
	ret = AuthorDetail.objects.filter(telephone__startswith="110").values("author__name")

	print(ret)

	return HttpResponse("query")
