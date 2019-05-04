# -*- coding: utf-8 -*-

from django.conf import settings


def init_permision(request, current_user):
	"""
	用户权限初始化
	:param request:  请求相关所有数据
	:param current_user: 当前用户对象
	:return:
	"""

	# 根据当前用户信息获取此用户所拥有的所有权限，并放入Session
	# 从用户对象通过 角色字段，跨到角色表，在从角色表通过permission字段跨到权限表
	# 当前用户的所有权限 (queryset 不能放到session中)
	permission_queryset = current_user.roles.filter(permissions__isnull=False).values("permissions__id",
	                                                                                  "permissions__title",
	                                                                                  "permissions__url",
	                                                                                  "permissions__name",
	                                                                                  "permissions__pid",
	                                                                                  "permissions__pid__title",
	                                                                                  "permissions__pid__url",
	                                                                                  "permissions__menu_id",
	                                                                                  "permissions__menu__title",
	                                                                                  "permissions__menu__icon",
	                                                                                  ).distinct()

	"""
	"permissions__id",          权限 id
	"permissions__title",       权限 title
	"permissions__url",         权限 url
	"permissions__pid_id",      父权限 id  # 用于点击非菜单按钮时，默认选中二级菜单
	"permissions__pid__title",  父权限 title   # 用于路径导航
	"permissions__pid___url",   父权限 url      # 用于路径导航
	"permissions__menu_id",     一级菜单  id
	"permissions__menu__title", 一级菜单 title
	"permissions__menu__icon"   一级菜单  icon
	
	"""
	# 获取权限+菜单信息
	permission_dict = {}
	menu_dict = {}

	for item in permission_queryset:
		permission_dict[item["permissions__name"]] = {
				'id': item["permissions__id"],
				'title': item["permissions__title"],
				'url': item["permissions__url"],
				'pid': item["permissions__pid"],
				'p_title': item["permissions__pid__title"],
				'p_url': item["permissions__pid__url"],
			}

		menu_id = item["permissions__menu_id"]
		node = {'id': item["permissions__id"], 'title': item["permissions__title"], 'url': item["permissions__url"]}
		if not menu_id: continue
		if menu_id in menu_dict:
			menu_dict[menu_id]['children'].append(node)
		else:
			menu_dict[menu_id] = {
				'title': item["permissions__menu__title"],
				'icon': item["permissions__menu__icon"],
				'children': [node, ]
			}

	request.session[settings.PERMISSION_SESSION_KEY] = permission_dict
	request.session[settings.MENU_SESSION_KEY] = menu_dict
