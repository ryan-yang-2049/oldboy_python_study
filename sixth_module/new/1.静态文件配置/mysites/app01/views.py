from django.shortcuts import render

import time
# Create your views here.

def timer(request):

	ctime = time.time()
	return render(request,'timer.html',{"now_time":ctime})