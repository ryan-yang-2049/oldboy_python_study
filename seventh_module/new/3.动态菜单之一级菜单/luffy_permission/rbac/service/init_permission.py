# -*- coding: utf-8 -*-

# __title__ = 'init_permission.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.10.11'

from django.conf import settings

def init_permission(current_user,request):
	"""
	用户权限的初始化
	:param current_user:当前用户对象
	:param request: 请求相关的所有数据
	:return:
	"""
	# 根据当前用户信息获取此用户所拥有的所有权限，并放入session (queryset 不能直接放在session中，只能是python的数据类型)
	permissions_queryset = current_user.roles.filter(permissions__isnull=False).all().values("permissions__id","permissions__title","permissions__url","permissions__is_menu","permissions__icon").distinct()


	menu_list = []   # 权限url中的可作为菜单的url存入列表
	permission_list = []  # 用户的权限列表
	for item in permissions_queryset:
		permission_list.append(item['permissions__url'])
		if item["permissions__is_menu"]:    # 如果是菜单（True），则添加
			temp = {
				'title':item["permissions__title"],
				'icon':item["permissions__icon"],
				'url':item["permissions__url"],
			}
			menu_list.append(temp)


	# 获取权限列表 + 菜单信息
	permission_list = [ item['permissions__url'] for item in permissions_queryset]
	# 将权限信息放入session
	request.session[settings.PERMISSION_SESSION_KEY] = permission_list
	request.session[settings.MENU_SESSION_KEY] = menu_list







