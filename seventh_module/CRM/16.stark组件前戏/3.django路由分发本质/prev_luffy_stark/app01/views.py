from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):

	return HttpResponse("app01 index  ok")


def home(request):

	return HttpResponse("app01 home  ok")
