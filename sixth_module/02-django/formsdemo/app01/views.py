from django.shortcuts import render

# Create your views here.

#
# from django import forms
# from django.forms import widgets
#
# class UserForm(forms.Form):
# 	name = forms.CharField(min_length=4,label="用户名:",error_messages={"required":"用户名不能为空"})
# 	pwd = forms.CharField(min_length=4,label="密码:",error_messages={"required":"用户名不能为空"},widget=widgets.PasswordInput) # password 类型
# 	r_pwd = forms.CharField(min_length=4,label="确认密码:",error_messages={"required":"用户名不能为空"})
# 	email = forms.EmailField(label="邮箱:",error_messages={"required":"用户名不能为空", 'invalid': '格式错误'})
# 	tel = forms.CharField(label="手机号:",error_messages={"required":"用户名不能为空"})
#
#
#
#
#
#
# def reg(request):
#
# 	if request.method == "POST":
# 		# print(request.POST)
#
# 		# form = UserForm({"name":"ryan","email":"123","xxxxx":"cherry"})
#
# 		form = UserForm(request.POST)  # form的name属性值应该与forms组件的字段名称
#
#
# 		print(form.is_valid()) # 校验所有的字段，全部正确返回True，只要有一个错，就返回False
#
# 		if form.is_valid():
# 			print("1",form.cleaned_data)     #所有字段校验成功，检验成功的字段放入 form.cleaned_data
# 		else:
# 			print("2",form.cleaned_data)    # 包含检验成功的字段
# 			print("3",form.errors)          # 没有检验成功的字段
#
# 			return render(request, "reg.html", locals())
#
#
# 		# return HttpResponse("OK")
# 	form = UserForm()
#
#
# 	return render(request,"reg.html",locals())

# from django import forms
# from django.forms import widgets
#
# class UserForm(forms.Form):
# 	name = forms.CharField(min_length=4,label="用户名:",error_messages={"required":"用户名不能为空"})
# 	pwd = forms.CharField(min_length=4,label="密码:",error_messages={"required":"用户名不能为空"},widget=widgets.PasswordInput) # password 类型
# 	r_pwd = forms.CharField(min_length=4,label="确认密码:",error_messages={"required":"用户名不能为空"})
# 	email = forms.EmailField(label="邮箱:",error_messages={"required":"用户名不能为空", 'invalid': '格式错误'})
# 	tel = forms.CharField(label="手机号:",error_messages={"required":"用户名不能为空"})
#
# def reg(request):
#
# 	if request.method == "POST":
# 		form = UserForm(request.POST)  # form的name属性值应该与forms组件的字段名称
# 		print(form.is_valid()) # 校验所有的字段，全部正确返回True，只要有一个错，就返回False
# 		if form.is_valid():
# 			print("1",form.cleaned_data)     #所有字段校验成功，检验成功的字段放入 form.cleaned_data
# 		else:
# 			print("2",form.cleaned_data)    # 包含检验成功的字段
# 			print("3",form.errors)          # 没有检验成功的字段
# 			return render(request, "reg.html", locals())
# 	form = UserForm()
# 	return render(request,"reg.html",locals())


from django import forms
from django.forms import widgets
from app01.models import UserInfo

from django.core.exceptions import NON_FIELD_ERRORS, ValidationError

class UserForm(forms.Form):
	name = forms.CharField(min_length=4,label="用户名:",
	                       error_messages={"required":"用户名不能为空","min_length":"用户名最少4位"},
	                       widget=widgets.TextInput(attrs={"class":"form-control"}))
	pwd = forms.CharField(min_length=4,label="密码:",
	                      error_messages={"required":"密码不能为空"},
	                      widget=widgets.PasswordInput(attrs={"class": "form-control"})) # password 类型
	r_pwd = forms.CharField(label="确认密码:",
	                        error_messages={"required":"密码不能为空"},
	                        widget=widgets.TextInput(attrs={"class": "form-control"}))
	email = forms.EmailField(label="邮箱:",
	                         error_messages={"required":"邮箱不能为空", 'invalid': '格式错误'},
	                         widget=widgets.TextInput(attrs={"class": "form-control"})
	                         )
	tel = forms.CharField(label="手机号:",
	                      error_messages={"required":"手机号不能为空"},
	                      widget=widgets.TextInput(attrs={"class": "form-control"}))
	#局部钩子案例
	def clean_name(self):
		val = self.cleaned_data.get("name")
		ret = UserInfo.objects.filter(name=val)
		if not ret:
			return val
		else:
			raise ValidationError("该用户已存在！")
	# 全局钩子案例
	def clean(self):
		pwd=self.cleaned_data.get("pwd")
		r_pwd=self.cleaned_data.get("r_pwd")
		if pwd and r_pwd:
			if pwd == r_pwd:
				return self.cleaned_data
			else:
				raise ValidationError("两次密码不一致！")

def reg(request):
	if request.method == "POST":
		form = UserForm(request.POST)  # form的name属性值应该与forms组件的字段名称
		print(form.is_valid()) # 校验所有的字段，全部正确返回True，只要有一个错，就返回False
		if form.is_valid():
			print("1",form.cleaned_data)     #所有字段校验成功，检验成功的字段放入 form.cleaned_data
		else:
			print("2",form.cleaned_data)    # 包含检验成功的字段
			print("3",form.errors)          # 没有检验成功的字段
			# 全局钩子错误
			global_errors = form.errors.get("__all__")
			return render(request, "reg.html", locals())
	form = UserForm()
	return render(request,"reg.html",locals())