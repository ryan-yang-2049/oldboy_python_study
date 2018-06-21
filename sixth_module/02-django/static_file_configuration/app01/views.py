from django.shortcuts import render,HttpResponse
from django.urls import  reverse
# Create your views here.


def timer(request):
	import time
	ctime = time.time()
	return  render(request,'timer.html',{"ctime":ctime})


def special_case_2003(request):
	# HttpResponse 响应对象
	url = reverse('s_c_2003')
	print(url)  # /app01/articles/2003/
	return HttpResponse('special_case_2003')

def year_archive(request,year):
	url = reverse('y_a',args=(year,))
	print(url) # /app01/articles/2012/
	return HttpResponse('<p style="color: blue">%s year</p>'%year)

def month_archive(request,month,year):
	url = reverse('y_a',args=(1007,))
	print(url)  #/app01/articles/1007/
	return HttpResponse('<p style="color: blue">%s year %s month</p>'%(year,month))



def article_detail(request,month,day,year):
	return HttpResponse(year+'-'+month+'-'+day)



def login(request):
	# get请求直接拿到 login.html
	# post 请求直接验证 用户信息

	print("methon:",request.method)

	if request.method == "GET":
		print("GET:", request.GET)
		return render(request,"login.html")
	elif request.method == "POST":
		print("POST:", request.POST) # POST: <QueryDict: {'user': ['ryan'], 'pwd': ['1234']}>

		user = request.POST.get("user")
		pwd = request.POST.get("pwd")

		if user == 'ryan' and pwd == '123':
			return HttpResponse('登陆成功')
		else:
			return HttpResponse('登陆失败')


def index(request):

	return HttpResponse(reverse("app01:index"))

def path_year(request,year):
	print(year)
	print(type(year))
	return HttpResponse("year:%s"%(year))


def path_month(request,month):

	return HttpResponse("month:%d"%month)
