from django.shortcuts import render

# Create your views here.


def  index(request):
	'''
	模板语法：
		变量： {{ }}
			1.深度查询   句点符
			2.过滤器
	:param request:
	:return:
	'''

	info = {"name":"ryan","age":22}

	import datetime
	now_time = datetime.datetime.now()

	empty_list = []
	file_size = 1231212
	link = "<a href='#'>click</a>"

	return  render(request,"index.html",locals())