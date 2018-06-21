from django.shortcuts import render,HttpResponse

# Create your views here.


def welcome(request):
	return render(request,'welcome.html')
#
#
# def index(request):
#
# 	# 请求对象
# 	print("method:",request.method)  # GET请求 地址栏发请求默认都是GET请求
#
# 	print("request.GET  >>",request.GET)    # 存储所有GET请求信息
# 	print("GET name value: ",request.GET.get("name"))
# 	print("GET age value: ",request.GET.get("age"))
#
# 	print("request.POST >>",request.POST)   # 存储所有POST请求信息
# 	print("POST name value: ",request.POST.get("name"))
# 	print("POST age value: ",request.POST.get("age"))
#
# 	'''
# 	URL包含: 协议://IP:PORT/路径?参数(GET请求的数据)
# 	'''
# 	print("request directory:",request.path)   # 获取请求路径；/index/
#
# 	print("get_full_path:",request.get_full_path())   # 获取请求路径；/index/?name=ryan&age=19
#
# 	import time
# 	ctime = time.time()
#
# 	dic = {"ctime":ctime}
#
# 	return render(request,'index.html',dic)  # index.html:模板文件
	# render 先拿到模板文件，渲染成模板文件，转换成HTML文件以后才发送给用户。



def index(request):
	'''
	模板语法：
		变量：{{}}
			1. 深度查询  句点符
			2. 过滤器


		标签：{% %}
	:param request:
	:return:
	'''

	name = 'ryan'
	i = 10
	l = [11,22,33]
	info = {"name":"ryan","age":22}
	b = True
	class Person(object):
		def __init__(self,name,age):
			self.name=name
			self.age = age

	ryan = Person("ryan",22)
	cherry = Person("cherry",18)

	person_list = [ryan,cherry]

	return render(request,'index.html',locals())










