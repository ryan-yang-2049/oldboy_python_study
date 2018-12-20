视频 32-34

知识点：
	1.前端页面可以用safe把数字转换成字符串
	<tr class="{% if row.id|safe == menu_id %}active {% endif %}">
	
	
	2.点击跳转时保留原来搜索的地址
	例如: 
	http://127.0.0.1:8000/rbac/menu/list/?mid=2  点击新增 http://127.0.0.1:8000/rbac/menu/add/?_filter=mid%3D2
	_filter 里面保存的就是 request 的GET请求里面的 mid=2
	
	3.request.GET.urlencode() 可以获取url后面的所有GET参数请求 
	例如：
		http://127.0.0.1:8000/rbac/menu/list/?mid=2&name=ryan&age=20  就可以获取到 mid=2&name=ryan&age=20 
		
	
	
	4.QueryDict：
		from django.http import QueryDict
		QueryDict 可以将把GET请求里面的参数进行转义，得到上面2 知识点那样的 _filter=mid%3D2
		
		
	5.ModelFOrm
		class MenuModelForm(forms.ModelForm):

			class Meta:
				model = models.Menu
				fields = ['title','icon']
				widgets = {
					'title':forms.TextInput(attrs={'class':'form-control'}),
					'icon' :forms.RadioSelect(
						choices=[
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
						],
						attrs={'class':'clearfix'}
					)
				}
