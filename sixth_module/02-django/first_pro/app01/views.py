from django.shortcuts import render

# Create your views here.



def timer(request):   #request是必须的
	import time
	ctime = time.time()

	return render(request,"timer.html",{"date":ctime})



def login(request):

	return render(request,"login.html")

