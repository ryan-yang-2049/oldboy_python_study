from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):

	return HttpResponse("index  ok")


def home(request):

	return HttpResponse("home  ok")
