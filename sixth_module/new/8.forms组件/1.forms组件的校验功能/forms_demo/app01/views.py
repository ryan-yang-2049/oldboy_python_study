from django.shortcuts import render,HttpResponse

# Create your views here.


from django import forms

class UserForm(forms.Form):
	name = forms.CharField(min_length=4)
	pwd = forms.CharField(min_length=4) # password 类型
	r_pwd = forms.CharField(min_length=4)
	email = forms.EmailField()
	tel = forms.CharField()


def reg(request):
	if request.method == "POST":
		form = UserForm(request.POST)  # form的name属性值应该与forms组件的字段名称
		print(form.is_valid()) # 校验所有的字段，全部正确返回True，只要有一个错，就返回False
		if form.is_valid():
			print("1",form.cleaned_data)     #所有字段校验成功，检验成功的字段放入 form.cleaned_data
		else:
			print("2",form.cleaned_data)    # 包含检验成功的字段
			print("3",form.errors)          # 没有检验成功的字段
			return render(request, "reg.html", locals())
	return render(request,"reg.html",locals())
