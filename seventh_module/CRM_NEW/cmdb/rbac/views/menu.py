# -*- coding: utf-8 -*-

from collections import OrderedDict
from django.shortcuts import HttpResponse, render, redirect
from django.urls import reverse
from rbac.service.routes import get_all_url_dict
from rbac.forms.menuform import MenuModelForm, SecondMenuModelForm, PermissionModelForm, MultiAddPermissionForm, \
	MultiEditPermissionForm
from rbac import models
from rbac.service.parse_urls import memory_reverse


def menu_list(request):
	"""
	菜单展示
	:param request:
	:return:
	"""
	menu_queryset = models.Menu.objects.all()
	menu_id = request.GET.get('mid')  # 选择的一级菜单
	second_menu_id = request.GET.get('sid')  # 选择的一级菜单

	menu_exists = models.Menu.objects.filter(id=menu_id).exists()
	if not menu_exists:
		menu_id = None
	if menu_id:
		second_menus = models.Permission.objects.filter(menu_id=menu_id)
	else:
		second_menus = []

	permission_exists = models.Permission.objects.filter(id=second_menu_id).values("menu_id")
	if permission_exists:
		second_menu_exists = models.Permission.objects.filter(id=second_menu_id).values("menu__id").first()
		if not second_menu_exists["menu__id"]:
			second_menu_id = None
		if second_menu_id:
			permissions = models.Permission.objects.filter(pid_id=second_menu_id)
		else:
			permissions = []
	else:
		permissions = []

	return render(
		request,
		'rbac/menu_list.html',
		{
			"menus": menu_queryset,
			"menu_id": menu_id,
			"second_menu_id": second_menu_id,
			"second_menus": second_menus,
			"permissions": permissions
		})


def menu_add(request):
	"""
	添加角色
	:param request:
	:return:
	"""
	if request.method == "GET":
		form = MenuModelForm()
		return render(request, 'rbac/change.html', {'form': form})
	form = MenuModelForm(request.POST)
	if form.is_valid():
		form.save()
		return redirect(memory_reverse(request, "rbac:menu_list"))
	return render(request, 'rbac/change.html', {'form': form})


def menu_edit(request, pk):
	"""
	编辑一级菜单
	:param request:
	:param pk:
	:return:
	"""
	obj = models.Menu.objects.filter(pk=pk).first()
	if not obj: return HttpResponse("菜单不存在")

	if request.method == "GET":
		form = MenuModelForm(instance=obj)  # 传到页面的时候，会自带查到的值
		return render(request, 'rbac/change.html', {'form': form})

	form = MenuModelForm(instance=obj, data=request.POST)
	if form.is_valid():
		form.save()
		return redirect(memory_reverse(request, "rbac:menu_list"))
	return render(request, 'rbac/change.html', {'form': form})


def menu_del(request, pk):
	"""
	删除一级菜单
	:param request:
	:param pk:
	:return:
	"""
	origin_url = memory_reverse(request, "rbac:menu_list")

	if request.method == "GET":
		info = models.Menu.objects.filter(pk=pk).first()
		return render(request, 'rbac/delete.html', {'info': info, "cancel": origin_url})

	models.Menu.objects.filter(pk=pk).delete()
	return redirect(origin_url)


def second_menu_add(request, menu_id):
	"""
	添加二级菜单
	:param request:
	:param menu_id: 已选择的一级菜单ID，(用于设置默认值)
	:return:
	"""
	menu_obj = models.Menu.objects.filter(id=menu_id).first()

	if request.method == "GET":
		form = SecondMenuModelForm(initial={'menu': menu_id})  # 返回页面时的默认值
		return render(request, 'rbac/change.html', {'form': form})
	form = SecondMenuModelForm(request.POST)
	if form.is_valid():
		form.save()
		return redirect(memory_reverse(request, "rbac:menu_list"))
	return render(request, 'rbac/change.html', {'form': form})


def second_menu_edit(request, pk):
	"""
	编辑二级菜单
	:param request:
	:param pk: 当前要编辑的二级菜单
	:return:
	"""
	permission_obj = models.Permission.objects.filter(pk=pk).first()

	if request.method == "GET":
		form = SecondMenuModelForm(instance=permission_obj)  # 传到页面的时候，会自带查到的值，也就是页面上显示的默认值
		return render(request, 'rbac/change.html', {'form': form})

	form = SecondMenuModelForm(instance=permission_obj, data=request.POST)  # 保存的时候，要把默认值也携带上
	if form.is_valid():
		form.save()
		return redirect(memory_reverse(request, "rbac:menu_list"))
	return render(request, 'rbac/change.html', {'form': form})


def second_menu_del(request, pk):
	"""
	删除二级菜单
	:param request:
	:param pk:
	:return:
	"""
	origin_url = memory_reverse(request, "rbac:menu_list")

	if request.method == "GET":
		info = models.Permission.objects.filter(pk=pk).first()
		return render(request, 'rbac/delete.html', {'info': info, "cancel": origin_url})

	models.Permission.objects.filter(pk=pk).delete()
	return redirect(origin_url)


def permission_add(request, second_menu_id):
	"""
	添加非菜单权限
	:param request:
	:param second_menu_id:
	:return:
	"""
	if request.method == "GET":
		form = PermissionModelForm()
		return render(request, 'rbac/change.html', {'form': form})
	form = PermissionModelForm(data=request.POST)
	if form.is_valid():
		second_menu_object = models.Permission.objects.filter(id=second_menu_id).first()
		if not second_menu_object:
			return HttpResponse("二级菜单不存在，请重新选中")
		form.instance.pid = second_menu_object
		"""
		此时的 form.instance .pid = second_menu_object 相当于
		instance.pid = second_menu_object
		instance = models.Permission(title='',name='',url='',pid=second_menu_object)
		"""
		form.save()
		return redirect(memory_reverse(request, "rbac:menu_list"))
	return render(request, 'rbac/change.html', {'form': form})


def permission_edit(request, pk):
	"""
	编辑非菜单权限
	:param request:
	:param pk: 当前要编辑的权限ID
	:return:
	"""
	print(pk)
	permission_obj = models.Permission.objects.filter(id=pk).first()
	print(permission_obj)
	if request.method == "GET":
		form = PermissionModelForm(instance=permission_obj)  # 传到页面的时候，会自带查到的值，也就是页面上显示的默认值
		return render(request, 'rbac/change.html', {'form': form})

	form = PermissionModelForm(instance=permission_obj, data=request.POST)  # 保存的时候，要把默认值也携带上
	if form.is_valid():
		form.save()
		return redirect(memory_reverse(request, "rbac:menu_list"))
	return render(request, 'rbac/change.html', {'form': form})


def permission_del(request, pk):
	"""
	删除非菜单权限
	:param request:
	:param pk:
	:return:
	"""
	origin_url = memory_reverse(request, "rbac:menu_list")

	if request.method == "GET":
		info = models.Permission.objects.filter(pk=pk).first()
		return render(request, 'rbac/delete.html', {'info': info, "cancel": origin_url})

	models.Permission.objects.filter(pk=pk).delete()
	return redirect(origin_url)


"""
formset 
	Form组件或ModelForm组件用于一个表单验证。
	formset用于做多个表单验证的组件
	应用场景：批量操作
	如何实现formset？
自动发现项目中的URL：
	问题：给你一个项目，请帮我获取当前项目中都有哪些URL以及name，   例如: rbac:permission_list
	实现思路:
"""

from django.forms import formset_factory


def multi_permissions(request):
	"""
	批量操作权限
	:param request:
	:return:
	"""
	post_type = request.GET.get('type')
	generate_formset_class = formset_factory(MultiAddPermissionForm, extra=0)
	update_formset_class = formset_factory(MultiEditPermissionForm, extra=0)

	generate_formset = None
	update_formset = None
	if request.method == 'POST' and post_type == 'generate':
		# "批量增加"
		formset = generate_formset_class(data=request.POST)
		if formset.is_valid():
			object_list = []
			post_row_list = formset.cleaned_data
			has_error = False
			for i in range(0, formset.total_form_count()):
				row_dict = post_row_list[i]  # 拿到每一行的数据
				try:
					new_object = models.Permission(**row_dict)  # 实例化一个对象
					new_object.validate_unique()
					object_list.append(new_object)  # 用于批量增加
				except Exception as e:
					formset.errors[i].update(e)
					generate_formset = formset  # 页面上去展示错误信息
					has_error = True
			if not has_error:
				models.Permission.objects.bulk_create(object_list, batch_size=100)  # 批量增加100条
		else:
			generate_formset = formset

	if request.method == 'POST' and post_type == 'update':
		# "批量更新"
		formset = update_formset_class(data=request.POST)
		if formset.is_valid():
			post_row_list = formset.cleaned_data

			for i in range(0, formset.total_form_count()):
				row_dict = post_row_list[i]
				permission_id = row_dict.pop('id')
				try:
					row_object = models.Permission.objects.filter(id=permission_id).first()
					for k, v in row_dict.items():
						setattr(row_object, k, v)
					row_object.validate_unique()
					row_object.save()
				except Exception as e:
					formset.errors[i].update(e)
					update_formset = formset
		else:
			update_formset = formset

	# 1.获取 自动发现  项目中所有的URL
	all_url_dict = get_all_url_dict()
	"""
	all_url_dct = {
		' rbac:user_list':{'name': 'rbac:user_list', 'url': '/rbac/user/list/'},
		' rbac:user_add':{'name': 'rbac:user_add', 'url': '/rbac/user/add/'},
		' rbac:user_edit':{'name': 'rbac:user_edit', 'url': '/rbac/user/edit/(?P<pk>\\d+)/'},
		' rbac:user_del':{'name': 'rbac:user_del', 'url': '/rbac/user/del/(?P<pk>\\d+)/'},
	}"""
	router_name_set = set(all_url_dict.keys())  # 获取项目中所有URL的name 'rbac:user_del'

	# 2.获取数据库中所有的URL
	permissions = models.Permission.objects.all().values('id', 'title', 'name', 'url', 'menu_id',
	                                                     'pid_id')  # QuerySet类型

	permission_dict = OrderedDict()
	permission_name_set = set()  # 数据库中的name集合。
	for row in permissions:
		permission_dict[row['name']] = row
		permission_name_set.add(row['name'])
	"""
	permission_dict{
	    'rbac:role_list': {'id':1,'title':'角色列表',name:'rbac:role_list',url.....},
	    'rbac:role_add': {'id':1,'title':'添加角色',name:'rbac:role_add',url.....},
	    ...
	}
	"""
	for name, value in permission_dict.items():
		router_row_dict = all_url_dict.get(name)
		if not router_row_dict: continue
		if value['url'] != router_row_dict['url']:
			value['url'] = '路由和数据库中不一致，请检查！'
		# value['url'] = value['url'] +"$$$"+ router_row_dict['url']

	# 3.应该添加，删除，修改的权限有哪些
	# 3.1 自动发现的权限 "大于" 数据库中的权限  --> 实现批量添加url 的name
	if not generate_formset:
		generate_name_list = router_name_set - permission_name_set
		generate_formset = generate_formset_class(
			initial=[row_dict for name, row_dict in all_url_dict.items() if
			         name in generate_name_list])  # 自动发现有，数据库没有，就放到页面去展示，并批量添加

	# 3.2 数据库中的权限 "大于"  自动发现的权限  --> 批量删除
	delete_name_list = permission_name_set - router_name_set
	delete_row_list = [row_dict for name, row_dict in permission_dict.items() if name in delete_name_list]

	# 3.3 自动发现的权限 和数据库中的权限 个数一致，值有不一致的
	# {'payment_list', 'payment_del', 'customer_tpl', 'customer_del', 'customer_import', 'payment_add', 'customer_edit', 'payment_edit', 'customer_list', 'customer_add'}
	if not update_formset:
		update_name_list = permission_name_set & router_name_set
		update_formset = update_formset_class(
			initial=[row_dict for name, row_dict in permission_dict.items() if name in update_name_list])
	return render(request, 'rbac/multi_permission.html', {
		'generate_formset': generate_formset,
		'delete_row_list': delete_row_list,
		'update_formset': update_formset,
	})


def multi_permissions_del(request, pk):
	"""
	批量页面的权限删除
	:param request:
	:param pk:
	:return:
	"""
	origin_url = memory_reverse(request, "rbac:multi_permissions")

	if request.method == "GET":
		info = models.Permission.objects.filter(pk=pk).first()
		return render(request, 'rbac/delete.html', {'info': info, "cancel": origin_url})

	models.Permission.objects.filter(pk=pk).delete()
	return redirect(origin_url)


"""
知识点
	- formset (ModelFormSet)
	- 自动发现项目中的URL
	- 唯一约束错误信息
	
"""

"""
权限分配
	- 展示用户，角色，权限信息
	- 选择用户、角色时，页面上的默认选项
	- 角色和权限的保存与分配
"""
from django.conf  import settings
from django.utils.module_loading import import_string
def distribute_permission(request):
	"""
	权限分配
	:param request:
	:return:
	"""
	user_id = request.GET.get('uid')  # 页面选中的用户ID
	# 业务中的用户表
	user_model_class = import_string(settings.RBAC_USER_MODEL_CLASS)
	user_object = user_model_class.objects.filter(id=user_id).first()
	if not user_object:
		user_id = None

	role_id = request.GET.get('rid')
	role_object = models.Role.objects.filter(id=role_id).first()
	if not role_object:
		role_id = None

	if request.method == "POST":
		if request.POST.get("type") == "role":
			roles_id_list = request.POST.getlist('roles')
			print("roles_id_list", roles_id_list)
			# 用户和角色的关系添加到第三张表 many to many
			if not user_object:
				return HttpResponse('请选择用户,然后在分配角色')
			user_object.roles.set(roles_id_list)    # 用户和角色表是多对多关系，set是绑定多对多关系

		elif request.POST.get("type") == "permission":
			permission_id_list = request.POST.getlist('permissions')
			if not role_object:
				return HttpResponse("请选择角色,然后在分配权限")
			role_object.permissions.set(permission_id_list)

	# 获取当前用户拥有的所有角色
	if user_id:
		user_has_roles = user_object.roles.all()
	else:
		user_has_roles = []
	user_has_roles_dict = {item.id: None for item in user_has_roles}
	# print("user_has_roles_dict", user_has_roles_dict)

	# 获取当前用户拥有的所有权限

	# 如果选中了角色，优先显示选中角色所拥有的权限
	# 如果没有选择角色，才显示用户所拥有的权限
	if role_object:  # 选择了角色
		user_has_permissions = role_object.permissions.all()
		user_has_permissions_dict = {item.id: None for item in user_has_permissions}
	elif user_object:  # 未选择角色，但选择了用户
		user_has_permissions = user_object.roles.filter(permissions__isnull=False).values('id',
		                                                                                  'permissions').distinct()
		user_has_permissions_dict = {item['permissions']: None for item in user_has_permissions}
	else:
		user_has_permissions = {}

	all_user_list = user_model_class.objects.all()

	all_role_list = models.Role.objects.all()

	menu_permission_list = []
	# 所有的一级菜单
	all_menu_list = models.Menu.objects.all().values('id', 'title')

	all_menu_dict = {}

	for item in all_menu_list:
		item['children'] = []
		all_menu_dict[item['id']] = item

	# 获取所有的二级菜单 (menu 不为空)
	all_second_menu_list = models.Permission.objects.filter(menu__isnull=False).values('id', 'title', 'menu_id')
	all_second_menu_dict = {}

	for row in all_second_menu_list:
		row['children'] = []
		all_second_menu_dict[row['id']] = row
		menu_id = row['menu_id']
		all_menu_dict[menu_id]['children'].append(row)

	# 获取所有三级菜单 （不能做菜单的权限）
	all_permission_list = models.Permission.objects.filter(pid_id__isnull=False).values('id', 'title', 'pid_id')

	for permission in all_permission_list:
		pid = permission['pid_id']
		if not pid:
			continue
		all_second_menu_dict[pid]['children'].append(permission)

	# print(all_menu_dict)
	return render(request, 'rbac/distribute_permission.html', locals())

"""
知识点：
	- 数据类型设置引用
	- ManyToMany role_object.permissions.set(permission_id_list)
	- 页面返回类型判断：可以是form的action，或者是 input设置隐藏返回name
"""