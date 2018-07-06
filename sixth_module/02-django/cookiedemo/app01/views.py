from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

from app01.models import  UserInfo

def login(request):


	if request.method == "POST":
		user=request.POST.get("user")
		pwd=request.POST.get("pwd")
		user_info = UserInfo.objects.filter(user=user,pwd=pwd).first()

		if user_info:

			'''
			响应体：
			return HttpResponse()
			return redirect()
			return render()
			'''
			print("登陆成功")
			# response = HttpResponse("登陆成功")
			response = redirect('/index/')

			# response.set_cookie("is_login",True,max_age=15)    #max_age 延时时间，秒(s)为单位
			response.set_cookie("is_login",True)
			import datetime
			# date=datetime.datetime(year=2019,month=7,day=6,hour=8,minute=10,second=30)
			# response.set_cookie("username",user_info.user,expires=date)  # expires 以具体的时间为单位，UTC的时间，所以，本地时间要-8
			response.set_cookie("username",user_info.user,path="/index")

			return response

	return render(request,"login.html")


def index(request):



	is_login = request.COOKIES.get("is_login")

	if is_login:
		username = request.COOKIES.get("username")
		import datetime
		now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

		last_time = request.COOKIES.get("last_visit_time","")
		response = render(request, "index.html", locals())
		response.set_cookie("last_visit_time",now)
		return response
	else:
		return redirect("/login/")

def order(request):
	print(request.COOKIES)
	is_login = request.COOKIES.get("is_login")

	if is_login:
		username = request.COOKIES.get("username")
		return render(request, "index.html", locals())
	else:
		return redirect("/login/")
