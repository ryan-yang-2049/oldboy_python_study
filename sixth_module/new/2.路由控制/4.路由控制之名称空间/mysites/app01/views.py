from django.shortcuts import render,HttpResponse
from django.urls import reverse

import time
# Create your views here.

def index(request):

	url =reverse('index01:index')

	return HttpResponse(url)