from django.shortcuts import render,HttpResponse,redirect

# Create your views here.


'''
用户认证组件：
	功能：用session记录登陆验证状态
	前提：用户表：django自带的auth_user  (需要添加字段时可以：1.继承这张表，2.做一对一的映射方式)
	
	创建超级用户：python3 manage.py createsuperuser
	API:
		from django.contrib import  auth
			1. authenticate # if 验证成功,返回user_obj对象,否则返回None
						 user_obj=auth.authenticate(username=user,password=pwd)
			2. auth.login(request,user_obj)  # 意味着：request.user==user_obj ,request.user:当前登陆对象
			3. auth.logout(request)  #注销
		from django.contrib.auth.models import User    # auth_user
			1.request.user.is_authenticated # True or False
			2.User.objects.create_user(username=user,password=pwd)  #创建用户(超级用户：create_superuser)
			
	补充：
		匿名用户对象
		    class models.AnonymousUser
		
		    django.contrib.auth.models.AnonymousUser 类实现了django.contrib.auth.models.User 接口，但具有下面几个不同点：
		
		    id 永远为None。
		    username 永远为空字符串。
		    get_username() 永远返回空字符串。
		    is_staff 和 is_superuser 永远为False。
		    is_active 永远为 False。
		    groups 和 user_permissions 永远为空。
		    is_anonymous() 返回True 而不是False。
		    is_authenticated() 返回False 而不是True。
		    set_password()、check_password()、save() 和delete() 引发 NotImplementedError。
		    New in Django 1.8:
		    新增 AnonymousUser.get_username() 以更好地模拟 django.contrib.auth.models.User。
	
	总结：
	
		request.user
			if not : auth.login(request.user)     request.user == AnonymousUser()
			else: request.user == 登陆对象   #request.user 是全局变量，它可以在任何视图和模板中使用。

'''
from django.contrib import  auth
from django.contrib.auth.decorators import login_required
# 登陆
def login(request):
	if request.method == "POST":
		user = request.POST.get("user")
		pwd = request.POST.get("pwd")
		# if 验证成功,返回user_obj对象,否则返回None
		user_obj=auth.authenticate(username=user,password=pwd)
		if user_obj:
			# 注册session
			auth.login(request,user_obj)  # 意味着：request.user==user_obj ,request.user:当前登陆对象
			next_url = request.GET.get("next","/index/")
			return redirect(next_url)
	return render(request,"login.html")
# 首页
# @login_required
def index(request):
	print("request.user:",request.user.username)      # 未登录时 AnonymousUser
	print("request.id:",request.user.id)      # 未登录时 AnonymousUser
	print("request.is_anonymous:",request.user.is_anonymous)      # 未登录时 AnonymousUser
	# if request.user.is_anonymous:
	# if not request.user.is_authenticated:
	# 	return redirect("/login/")
	username = request.user.username
	return render(request,"index.html",locals())
# 注销
def loginout(request):
	auth.logout(request)
	return redirect("/login/")
#注册
from django.contrib.auth.models import User
def reg(request):
	if request.method == "POST":
		user = request.POST.get("user")
		pwd = request.POST.get("pwd")
		user_obj = User.objects.create_user(username=user,password=pwd)
		return redirect("/login/")
	return render(request,"reg.html")
# 订单页面
# @login_required
def order(request):
	# if not request.user.is_authenticated:
	# 	return redirect("/login/")
	return render(request,"order.html")


