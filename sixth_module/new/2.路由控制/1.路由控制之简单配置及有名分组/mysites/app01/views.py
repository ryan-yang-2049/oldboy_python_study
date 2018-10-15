from django.shortcuts import render,HttpResponse

import time
# Create your views here.

def timer(request):

	ctime = time.time()
	return render(request,'timer.html',{"now_time":ctime})


def special_case_2003(request):


	return HttpResponse("special_case_2003")


def year_archive(request,year):


	return HttpResponse(year)


def month_archive(request,year,month):


	return HttpResponse(year+"年"+month+"月")


def article_detail(request,year,month,day):


	return HttpResponse(year+"年"+month+"月"+day+"日")
