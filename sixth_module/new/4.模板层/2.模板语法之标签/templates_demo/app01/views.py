from django.shortcuts import render,HttpResponse

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


	# 模板语法之标签

	list = [1,'a',2,'b',3,'c']


	info = {"name":"ryan","age":22}

	return  render(request,"index.html",locals())


def login(request):

	if request.method == "POST":
		return HttpResponse("OK  POST........")

	return render(request,"login.html",locals())