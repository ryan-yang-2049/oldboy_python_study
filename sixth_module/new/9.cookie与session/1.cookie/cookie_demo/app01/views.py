from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
from app01.models import UserInfo

def login(request):
	if request.method == "POST":
		user = request.POST.get("user")
		pwd = request.POST.get("pwd")
		user_info = UserInfo.objects.filter(user=user, pwd=pwd).first()
		if user_info:

			response = redirect('/index/')
			#设置网页超时时间
			# response.set_cookie("is_login",True,max_age=10)    #max_age 延时时间，秒(s)为单位
			response.set_cookie("is_login", True)
			import datetime
			# date=datetime.datetime(year=2019,month=7,day=6,hour=8,minute=10,second=30)
			# response.set_cookie("username",user_info.user,expires=date,path="/index")  # expires 以具体的时间为单位，UTC的时间，所以，本地时间要-8
			response.set_cookie("username", user_info.user, path="/index/")
			# path 如果设置了,那么该cookie只针对有效的路径有效，别的无效。如果不设置，那么全局有效
			return response
	return render(request, "login.html")

def index(request):
	print("index",request.COOKIES)
	is_login = request.COOKIES.get("is_login")
	if is_login:
		username = request.COOKIES.get("username")
		# 上次登陆时间
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
