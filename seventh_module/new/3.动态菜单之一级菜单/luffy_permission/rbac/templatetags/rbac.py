# -*- coding: utf-8 -*-
"""
__title__ = 'rbac.py'
__author__ = 'ryan'
__mtime__ = '2018/10/11'
"""


from  django.template import Library

from django.conf import settings

register = Library()

@register.inclusion_tag('rbac/static_menu.html')
def  static_menu(request):
	"""
	创建一级菜单
	:return:
	"""

	menu_list = request.session.get(settings.MENU_SESSION_KEY)
	return {'menu_list':menu_list}




