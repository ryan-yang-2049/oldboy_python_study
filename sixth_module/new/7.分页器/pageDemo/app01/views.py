from django.shortcuts import render,HttpResponse,redirect

from django.core.paginator import  Paginator,EmptyPage


# Create your views here.
from app01.models import Book
def insert_data(request):
	book_list = []
	for i in range(100):
		book = Book(title="book_%s"%i,price=i*i) # 实例对象
		book_list.append(book)
	Book.objects.bulk_create(book_list)
	return HttpResponse("OK")

def index(request):
	# 获取整个数据信息
	book_list = Book.objects.all()
	#分页器 Paginator(数据信息,每次显示的个数)
	paginator_obj = Paginator(book_list,3)
	print("paginator_obj",paginator_obj)
	# 浏览器发送get请求后，发送的page的值，如果page没有值，默认为 1
	current_page_num = int(request.GET.get("page", 1))
	# print(paginator_obj.count)  #数据总数
	# print(paginator_obj.num_pages)  #总页数
	# print(paginator_obj.page_range) #页码的列表

	# 分页按照左右各显示5个进行展示
	# 如果信息量超过10页
	if paginator_obj.num_pages>11:
		# 当get请求的page小于5时，就只在页面上显示1,11 页
		if current_page_num - 5 <1:
			page_range=range(1,12)
		# 当get请求的page+5大于总页数时，页面上显示最后11 页
		elif current_page_num +5 > paginator_obj.num_pages:
			page_range=range(paginator_obj.num_pages-10,paginator_obj.num_pages+1)
		else:
			page_range =range(current_page_num-5,current_page_num+6)
	else:
		page_range = paginator_obj.page_range
	try:
		current_page = paginator_obj.page(current_page_num)
		print("object_list",current_page.object_list) #每一页的显示的内容(对象)
	except EmptyPage as e:
		current_page=paginator_obj.page(1)

	# print("是否有下一页",current_page.has_next())    #是否有下一页 返回bool
	# print("下一页的页码",current_page.next_page_number())  #下一页的页码 如果没有会报错
	# print("是否有上一页",current_page.has_previous())  #是否有上一页 返回bool
	# print("上一页的页码",current_page.previous_page_number()) #上一页的页码 如果没有会报错
	return render(request,"index.html",locals())

