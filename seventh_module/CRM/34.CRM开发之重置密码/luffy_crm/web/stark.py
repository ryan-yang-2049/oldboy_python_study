# -*- coding: utf-8 -*-

# __title__ = 'stark.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.12.24'


from django.shortcuts import HttpResponse,redirect,render
from django.utils.safestring import mark_safe
from django.conf.urls import url

from stark.service.v1 import site, StarkHandler,get_choice_text,Option
from web import models
from stark.utils.parse_url import ParseUrl
from web.forms.user_form import UserInfoChangeModelForm,UserInfoAddModelForm,ResetPasswordForm
from web.utils.md5 import gen_md5

class SchoolHandler(StarkHandler):
	list_display = ['title']

site.registry(models.School, SchoolHandler)


class DepartmentHandler(StarkHandler):
	list_display = ['title']

site.registry(models.Department,DepartmentHandler)



class UserInfoHandler(StarkHandler):
	def display_reset_pwd(self,obj=None,is_header=None):
		if is_header:
			return "重置密码"
		parse_url = ParseUrl(request=self.request, namespace=self.site.namespace, name=self.get_reset_pwd_url_name, pk=obj.pk)
		url = parse_url.memory_url()
		return mark_safe('<a href="%s">重置密码</a>'%url)

	list_display = ['nickname','name',get_choice_text('性别','gender'),'phone','email','depart',display_reset_pwd]

	def get_model_form_class(self,is_add=False):
		if is_add:
			return UserInfoAddModelForm
		return UserInfoChangeModelForm

	def reset_password(self,request,pk):
		"""
		重置密码的视图函数
		:param request:
		:param pk:
		:return:
		"""
		userinfo_object = models.UserInfo.objects.filter(id=pk).first()
		if not  userinfo_object:
			return HttpResponse("用户不存在，无法进行重置！")
		if request.method == "GET":
			form =  ResetPasswordForm()
			return render(request,'stark/change.html',{'form':form})
		form = ResetPasswordForm(data=request.POST)
		if form.is_valid():
			userinfo_object.password = form.cleaned_data['password']
			userinfo_object.save()
			parse_url = ParseUrl(request=self.request, namespace=self.site.namespace, name=self.get_list_url_name)
			url = parse_url.memory_url()
			return redirect(url)
		return render(request, 'stark/change.html', {'form': form})

	@property
	def get_reset_pwd_url_name(self):

		return self.get_url_name('reset_pwd')

	def extra_urls(self):
		patterns = [
			url(r'^reset/password/(?P<pk>\d+)/$', self.wrapper(self.reset_password), name=self.get_reset_pwd_url_name)
		]

		return patterns

	search_list = ['nickname__contains','name__contains']

	search_group = [
		Option(field='gender'),
		Option(field='depart',is_multi=True),
	]

site.registry(models.UserInfo,UserInfoHandler)










