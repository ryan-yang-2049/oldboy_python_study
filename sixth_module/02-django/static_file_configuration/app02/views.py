from django.shortcuts import render,HttpResponse
from django.urls import reverse

# Create your views here.

def index(request):


	return HttpResponse(reverse("app02:index"))