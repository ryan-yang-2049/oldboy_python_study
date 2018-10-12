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
	# 根据当前用户信息获取此用户所拥有的所有权限以及权限所对应的菜单url，并放入session (queryset 不能直接放在session中，只能是python的数据类型)
	permissions_queryset = current_user.roles.filter(permissions__isnull=False).all().values(
																								"permissions__id",
																								"permissions__title",
																								"permissions__url",
																								"permissions__pid",
																								"permissions__pid__title",
																								"permissions__pid__url",
																								"permissions__menu_id",
																								"permissions__menu__title",
																								"permissions__menu__icon"
																							).distinct()

	permission_list = []  # 用户的权限列表

	menu_dict = {}   # 权限url中的可作为菜单的url存入字典

	for item in permissions_queryset:
		permission_list.append({
			'id':item['permissions__id'],
			'title':item['permissions__title'],
			'url':item['permissions__url'],
			'pid':item['permissions__pid'],
			'p_title':item['permissions__pid__title'],
			'p_url':item['permissions__pid__url'],

		})

		menu_id = item["permissions__menu_id"]
		if not menu_id:
			continue

		node = {'id':item['permissions__id'],'title':item["permissions__title"],'url':item["permissions__url"]}
		if menu_id in menu_dict:
			menu_dict[menu_id]['children'].append(node)
		else:
			menu_dict[menu_id] = {
				'title':item["permissions__menu__title"],
				'icon':item["permissions__menu__icon"],
				'children':[node,]
			}

	# print(menu_dict)

	# 将权限信息放入session
	request.session[settings.PERMISSION_SESSION_KEY] = permission_list
	request.session[settings.MENU_SESSION_KEY] = menu_dict







