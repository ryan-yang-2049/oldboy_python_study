视频 35-39
	二级菜单及权限分配知识点：
	
	1.点击一级菜单时展示对应的二级菜单，这个需要把一级菜单的id传递过去，然后，在permission中去获取对应的二级菜单
	
	2.点击二级菜单展示权限信息时要注意：
		1.二级菜单的必须是一个包含了menu_id的url权限。
	
	3.form.instance 包含了用户form表单提交的所有值。如果要设置一个字段的默认值，那么就得另行设置
		例如：form.instance.pid = second_menu_object
		form = PermissionModelForm(data=request.POST)
		if form.is_valid():
			second_menu_object = models.Permission.objects.filter(id=second_menu_id).first()
			if not  second_menu_object:
				return HttpResponse("二级菜单不存在，请重新选择！")
			# form.instance 中包含了用户提交的所有值
			# 这里相当于是增加了一个pid的值
			form.instance.pid = second_menu_object
			form.save()
			return redirect(memory_reverse_url(request,'rbac:menu_list'))
		
	
	4.在模板html中  1|safe  就可以把1 转换成字符串 "1" 了
	
	
	5.ModelForm的radio的定制
			ICON_LIST = [
			['fa-calendar-plus-o',mark_safe('<i class="fa fa-calendar-plus-o" aria-hidden="true"></i>')],
			['fa-calendar-times-o',mark_safe('<i class="fa fa-calendar-times-o" aria-hidden="true"></i>')],
			['fa-bug',mark_safe('<i class="fa fa-bug" aria-hidden="true"></i>')],
			['fa-bookmark-o',mark_safe('<i class="fa fa-bookmark-o" aria-hidden="true"></i>')],
			['fa-bus',mark_safe('<i class="fa fa-bus" aria-hidden="true"></i>')],
			['fa-cogs',mark_safe('<i class="fa fa-cogs" aria-hidden="true"></i>')],
			['fa-copyright',mark_safe('<i class="fa fa-copyright" aria-hidden="true"></i>')],
			['fa-envelope-open',mark_safe('<i class="fa fa-envelope-open" aria-hidden="true"></i>')],
			['fa-crosshairs',mark_safe('<i class="fa fa-crosshairs" aria-hidden="true"></i>')],
			['fa-flag',mark_safe('<i class="fa fa-flag" aria-hidden="true"></i>')],
			['fa-image',mark_safe('<i class="fa fa-image" aria-hidden="true"></i>')],
			['fa-life-ring',mark_safe('<i class="fa fa-life-ring" aria-hidden="true"></i>')],
			['fa-pie-chart',mark_safe('<i class="fa fa-pie-chart" aria-hidden="true"></i>')],
			['fa-road',mark_safe('<i class="fa fa-road" aria-hidden="true"></i>')],
			]
			class MenuModelForm(forms.ModelForm):

				class Meta:
					model = models.Menu
					fields = ['title','icon']
					widgets = {
						'title':forms.TextInput(attrs={'class':'form-control'}),
						'icon' :forms.RadioSelect(
							choices= ICON_LIST,
							attrs={'class':'clearfix'}
						)
					}
	
	
	6.BootStrapModelForm 定制样式
	如果都要用到form-control 的样式就可以继承这个类
		from django import forms

		class BootStrapMOdelForm(forms.ModelForm):
			# 统一给ModelForm生成的字段添加css 样式
			def __init__(self,*args,**kwargs):
				super(BootStrapMOdelForm,self).__init__(*args,**kwargs)
				for name,field in self.fields.items():
					field.widget.attrs['class'] = 'form-control'