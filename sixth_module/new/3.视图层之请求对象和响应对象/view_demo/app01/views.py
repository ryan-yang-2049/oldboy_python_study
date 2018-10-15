from django.shortcuts import render,HttpResponse,redirect

# Create your views here.


def index(request):
	# 请求对象
	print(request.method)   # 请求方式 GET/POST

	print(request.GET)  #  http://127.0.0.1:8000/index/?age=10&name=ryan  --->   <QueryDict: {'age': ['10'], 'name': ['ryan']}>
	print(request.POST) # <QueryDict: {'csrfmiddlewaretoken': ['Zlz8mZ....0WJGz3ytSl'], 'name': ['ryan'], 'age': ['123']}>
	print(request.path) # http://127.0.0.1:8000/index/?age=10&name=ryan ---> /index/ {请求路径},后面的 ?age=10&name=ryan 只是请求参数
	'''
			协议以及地址：http://127.0.0.1:8000 
			请求路径：/index/
			GET请求的参数：?age=10&name=ryan
			协议://IP:POST/路径?参数
	'''

	print("get_full_path:",request.get_full_path())     #  get_full_path: /index/?age=10&name=ryan   带参数
	return redirect('/index/')
	# return  render(request,"index.html")
	# return HttpResponse("OK")

#  响应对象  render,HttpResponse,redirect  三种方法




