from django.shortcuts import render,HttpResponse
from django.urls import reverse

import time
# Create your views here.




def path_year(request,year):
	print(year,type(year))

	return HttpResponse(year)


def path_year_month(request,year,month):

	print(month)
	print(type(month))
	return HttpResponse("path_year_month")

