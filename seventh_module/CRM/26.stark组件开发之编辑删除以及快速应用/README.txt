视频 78-80  stark组件开发之编辑删除以及快速应用
https://www.cnblogs.com/wupeiqi/articles/9979155.html


1.保留原搜索条件带pk参数：*args,**kwargs
	from django.urls import reverse
	from django.http import QueryDict

	class ParseUrl(object):
		"""
		保留原搜索条件
		"""
		def __init__(self,request,namespace,name,*args,**kwargs):
			self.request = request
			self.namespace= namespace
			self.name = name
			self.args = args
			self.kwargs = kwargs
			self.nameinfo = "%s:%s"%(self.namespace,self.name)

		def memory_reverse_url(self):
			"""
			保留搜索的url参数到新的页面
			:return:
			"""
			base_url = reverse(self.nameinfo,args=self.args,kwargs=self.kwargs)
			if not  self.request.GET:
				url = base_url
			else:
				param = self.request.GET.urlencode()
				new_query_dict = QueryDict(mutable=True)
				new_query_dict['_filter'] = param
				url = "%s?%s"%(base_url,new_query_dict.urlencode())

			return url

		def memory_url(self):
			"""
			页面提交以后返回原始搜索页面
			:return:
			"""
			base_url = reverse(self.nameinfo, args=self.args, kwargs=self.kwargs)
			params = self.request.GET.get("_filter")
			if not params:
				return base_url
			url = "%s?%s"%(base_url,params)
			return url


2.编辑以及删除页面
	def change_view(self, request, pk):
		"""
		编辑页面
		:param request:
		:return:
		"""
		# 当前编辑对象
		current_change_object = self.model_class.objects.filter(pk=pk).first()
		if not current_change_object:
			return HttpResponse("需要修改的对象不存在，请重新选择")

		model_form_class = self.get_model_form_class()
		if request.method == "GET":
			form = model_form_class(instance=current_change_object)
			return render(request,'stark/change.html',{"form":form})

		form = model_form_class(data=request.POST,instance=current_change_object)
		if form.is_valid():
			self.form_database_save(form,is_update=False)
			# 在数据库中保存成功后,跳转回列表页面（携带原来的参数）
			parse_url = ParseUrl(request=self.request,namespace=self.site.namespace,name=self.get_list_url_name)
			url = parse_url.memory_url()
			return redirect(url)
		return render(request, 'stark/change.html', {"form": form})

	def delete_view(self, request, pk):
		"""
		删除页面
		:param request:
		:param pk:
		:return:
		"""
		parse_url = ParseUrl(request=self.request, namespace=self.site.namespace, name=self.get_list_url_name)
		cancel = parse_url.memory_url()
		if request.method == "GET":
			return render(request,'stark/delete.html',locals())
		current_delete_object = self.model_class.objects.filter(pk=pk).delete()
		return redirect(cancel)


3.快速应用
	创建一个在app01/models.py 里面创建一个deploy的表
	然后应用到stark组件中



























