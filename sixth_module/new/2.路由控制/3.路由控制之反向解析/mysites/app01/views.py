from django.shortcuts import render,HttpResponse
from django.urls import reverse

import time
# Create your views here.

def timer(request):
	ctime = time.time()
	return render(request,'timer.html',{"now_time":ctime})


def special_case_2003(request):

	url = reverse('s_c_2003')
	url = reverse('y_a',args=('1234',))
	print("url===>",url)
	return HttpResponse("special_case_2003")


def year_archive(request,year):
	url = reverse('y_a',args=(year,))
	print("url===>",url)
	return HttpResponse(year)


def month_archive(request,year,month):
	return HttpResponse(year+"年"+month+"月")


def article_detail(request,year,month,day):
	return HttpResponse(year+"年"+month+"月"+day+"日")


def login(request):

	if request.method == "POST":
		username = request.POST.get("user")
		password = request.POST.get("pwd")
		print(username,password)
		return HttpResponse("OK")
	return render(request,'login.html')





