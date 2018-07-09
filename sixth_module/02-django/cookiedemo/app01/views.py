from django.shortcuts import render,HttpResponse,redirect
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


def login_session(request):

	if request.method == "POST":
		user = request.POST.get("user")
		pwd = request.POST.get("pwd")
		user_info = UserInfo.objects.filter(user=user,pwd=pwd).first()

		if user_info:
			request.session["is_login"] = True
			request.session["username"] = user_info.user

			import datetime
			now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
			request.session["last_visit_time"] = now

			'''
			if request.COOKIE.get("sessionid") :
				更新操作 (session-key("随机字符串")   session-data{"is_login":True,"username":"ryan"} )
			else：
				1.生成一个随机字符串
				2.response.set_cookis("sessionid","随机字符串")
				3.在django-session表中创建一条记录
					session-key("随机字符串")   session-data{"is_login":True,"username":"ryan"} 
			
			'''

			return redirect("/index_session/")



	return render(request,"login.html")


def index_session(request):

	print("is_login:",request.session.get("is_login"))
	'''
	1.request.COOKIE.get("is_login")  # 随机字符串
	2. 在 django-session表中过滤记录{session-key("随机字符串")   session-data{"is_login":True,"username":"ryan"} }
		obj = django-session.objects.filter(session-ket=随机字符串).first()
		
	3. obj.session-data.get("is_login")

	'''
	print("====>",request.session,type(request.session))
	is_login=request.session.get("is_login")
	username = request.session.get("username")
	last_time = request.session.get("last_visit_time")
	if not is_login:
		return  redirect("/login_session/")



	return render(request,"index.html",locals())



def loginout(request):

	#删除session
	# del request.session["is_login"]


	request.session.flush()
	'''
	randon_str = request.COOKIE.get("sessionid")
	django-session.object.filter(session_ket = randon_str).delete()
	response.delete_cookie("sessionid",randon_str)
	'''


	return redirect("/login/")




