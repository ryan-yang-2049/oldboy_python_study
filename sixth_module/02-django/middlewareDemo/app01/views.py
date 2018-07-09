from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
	print("index .....")
	我是报错内容
	return HttpResponse("index")

def index_new(request):
	return HttpResponse("index_new")