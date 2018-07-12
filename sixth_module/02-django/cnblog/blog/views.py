from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

from django.http import JsonResponse
from django.contrib import auth
from blog.models import UserInfo
from blog.utils.Myforms import UserForm
from blog.utils.validCode import get_valid_code_img
from blog import models
from django.db.models import Avg,Max,Min,Count


def login(request):
	if request.method == "POST":
		response = {"user": None, "msg": None}
		user = request.POST.get("user")
		pwd = request.POST.get("pwd")
		valid_code = request.POST.get("valid_code")

		valid_code_str = request.session.get("valid_code_str")
		if valid_code.upper() == valid_code_str.upper():
			user_obj = auth.authenticate(username=user, password=pwd)
			if user_obj:
				auth.login(request, user_obj)  # request.user == 当前登陆对象

				response["user"] = user_obj.username
			else:
				response["msg"] = "用户名或者密码错误"
		else:
			response["msg"] = "验证码错误"
		return JsonResponse(response)

	return render(request, "login.html")


# 随机验证码
def get_validCode_img(request):
	'''
	基于PIL模块动态生成响应状态码图片
	:param request:
	:return:
	'''
	data = get_valid_code_img(request)
	return HttpResponse(data)


def register(request):
	'''

	:param request:
	:return:
	'''
	if request.is_ajax():
		form = UserForm(request.POST)
		response = {"user_info": None, "msg": None}
		if form.is_valid():
			response["user_info"] = form.cleaned_data.get("user")
			user = form.cleaned_data.get("user")
			pwd = form.cleaned_data.get("pwd")
			email = form.cleaned_data.get("email")
			avatar_obj = request.FILES.get("avatar")
			extra = {}
			if avatar_obj:
				extra["avatar"] = avatar_obj
			UserInfo.objects.create_user(username=user, password=pwd, email=email, **extra)
		else:
			response["msg"] = form.errors
		return JsonResponse(response)
	form = UserForm()
	return render(request, "register.html", locals())


def logout(request):

	auth.logout(request)    #等价于 request.session.flush()
	return redirect("/login/")



def index(request):

	article_list = models.Article.objects.all()



	return render(request, "index.html",locals())


def home_site(request,username,**kwargs):
	'''
	个人站点视图参数
	:param request:
	:return:
	'''
	user_obj = UserInfo.objects.filter(username=username).first()
	if not user_obj:

		return render(request,"not_found.html")

	# 当前用户或者当前站点对应的所有文章

	# 查询当前用户站点对象(一对一)
	blog=user_obj.blog

	# 当前用户或当前站点对应的所有文章
	# 基于对象查询
	# article_list = user_obj.article_set.all()

	# 基于双下划线
	article_list = models.Article.objects.filter(user=user_obj)
	# kwargs 为了区分访问的是站点页面还是站点下的跳转页面
	if kwargs:
		condition = kwargs.get("condition")
		param = kwargs.get("param")
		if condition == "category":
			article_list = models.Article.objects.filter(user=user_obj).filter(category__title=param)
		elif condition == "tag":
			article_list = models.Article.objects.filter(user=user_obj).filter(tags__title=param)
		else:
			year,month = param.split("-")
			article_list = models.Article.objects.filter(user=user_obj).filter(create_time__year=year,create_time__month=month)



	# 每一个对象的表模型.objects.values('pk').annotate(聚合函数(关联表__统计字段)).values(表模型字段，以及统计的字段)
	# 查询每一个分类名称以及对应的文章数
	# article_num = models.Category.objects.values('pk').annotate(c=Count("article__title")).values("title","c")


	# 查询当前用户或者站点的每一个分类名称以及对应的文章数
	# cate_list = models.Category.objects.filter(blog=blog).values('pk').annotate(c=Count("article__title")).values_list("title", "c")
	# print("cate_list",cate_list)

	# 查询当前站点的每一个标签名称以及对应的文章数
	# tag_list = models.Tag.objects.filter(blog=blog).values('pk').annotate(c=Count("article")).values_list("title", "c")
	# print(tag_list)

	# 查询当前站点每一个月的的名称以及对应的文章数
	# ret = models.Article.objects.extra(select={"is_recent":"create_time >'2017-09-07'"}).values("title","is_recent")
	# 方式一：
	# date_list = models.Article.objects.filter(user=user_obj).extra(select={"y_m_date":"date_format(create_time,'%%Y-%%m')"}).values("y_m_date").annotate(c=Count('nid')).values_list("y_m_date","c")


	# 方式二
	# from django.db.models.functions import TruncMonth ,TruncDay    # 日期归档

	# date_list1 = models.Article.objects.filter(user=user_obj).annotate(month=TruncMonth("create_time")).values("month").annotate(c=Count("nid")).values_list("month","c")
	# print("ret>>>>>>>", ret)


	return render(request,"home_site.html",locals())

def get_classification_data(username):
	user_obj = UserInfo.objects.filter(username=username).first()
	blog = user_obj.blog
	cate_list = models.Category.objects.filter(blog=blog).values('pk').annotate(
		c=Count("article__title")).values_list("title", "c")
	tag_list = models.Tag.objects.filter(blog=blog).values('pk').annotate(c=Count("article")).values_list("title","c")
	date_list = models.Article.objects.filter(user=user_obj).extra(select={"y_m_date": "date_format(create_time,'%%Y-%%m')"}).values("y_m_date").annotate(c=Count('nid')).values_list("y_m_date", "c")

	return {"blog":blog,"cate_list":cate_list,"tag_list":tag_list,"date_list":date_list}


def article_detail(request,username,article_id):
	# 下面这几个变量可以分装在一个函数中，然后 home_site 也可以一起调用

	# contact = get_classification_data(username)
	article_obj = models.Article.objects.filter(pk=article_id).first()

	return render(request, "article_detail.html",locals())