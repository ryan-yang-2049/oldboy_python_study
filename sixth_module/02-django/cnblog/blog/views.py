from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

from django.http import JsonResponse
from django.contrib import auth
def login(request):

	if request.method == "POST":
		response={"user":None,"msg":None}
		user = request.POST.get("user")
		pwd = request.POST.get("pwd")
		valid_code = request.POST.get("valid_code")

		valid_code_str = request.session.get("valid_code_str")
		if valid_code.upper()==valid_code_str.upper():
			user_obj =auth.authenticate(username=user,password=pwd)
			if user_obj:
				auth.login(request,user_obj)   #request.user == 当前登陆对象

				response["user"] =user_obj.username
			else:
				response["msg"] = "用户名或者密码错误"
		else:
			response["msg"]="验证码错误"
		return JsonResponse(response)

	return render(request,"login.html")


# 随机验证码
def get_validCode_img(request):
	'''
	基于PIL模块动态生成响应状态码图片
	:param request:
	:return:
	'''

	from blog.utils.validCode import  get_valid_code_img
	data = get_valid_code_img(request)

	return HttpResponse(data)


from django import forms
from django.forms import widgets

wid_01=widgets.TextInput(attrs={"class":"form-control"})
wid_02=widgets.PasswordInput(attrs={"class":"form-control"})
wid_03=widgets.EmailInput(attrs={"class":"form-control"})
class UserForm(forms.Form):
	user=forms.CharField(max_length=32,label="用户名", widget=wid_01)
	pwd=forms.CharField(max_length=32,label="密码",widget=wid_02)
	re_pwd=forms.CharField(max_length=32,label="确认密码",widget=wid_02)
	email=forms.EmailField(max_length=32,label="邮箱",widget=wid_03)




def register(request):

	if request.is_ajax():
		print(request.POST)
		form = UserForm(request.POST)

		response = {"user":None,"msg":None}
		if form.is_valid():
			response["user"]=form.cleaned_data.get("user")
		else:
			print(form.cleaned_data)
			print(form.errors)
			response["msg"]=form.errors

		return JsonResponse(response)


	form = UserForm()

	return render(request,"register.html",locals())

def index(request):



	return render(request,"index.html")