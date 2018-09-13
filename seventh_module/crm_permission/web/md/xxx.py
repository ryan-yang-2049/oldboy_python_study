# -*- coding: utf-8 -*-

# __title__ = 'xxx.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.09.07'

import  re
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse


class CheckPermission(MiddlewareMixin):
	"""
	用户权限信息的校验
	"""

	def process_request(self,request):
		"""
		当用户请求刚进入触发执行
		:param request:
		:return:
		"""
		"""
		1.获取当前用户请求的URL
		2.获取当前用户在session中保存的权限列表 luffy_permission_url_list_key(views.py中生成的)
		3.权限信息匹配
		"""

		current_url = request.path_info     # 请求的url
		# 访问路径白名单
		white_url_list = [
			'/login/',
			'/admin/.*',
		]
		for white_url in white_url_list:
			if re.match(white_url,current_url):
				#白名单中的url无需权限验证即可访问
				return  None



		permission_list = request.session.get('luffy_permission_url_list_key')
		if not permission_list:
			return HttpResponse("未获取到用户权限信息，请登录！")

		# print(current_url)
		# print(permission_list)
		# print(type(permission_list))

		flag = False
		for url in permission_list:
			reg = "^%s$" %url       # 精确匹配用户请求路径，如果没有^$ 那么 在匹配的时候， /customer/list/ 也能匹配到 /customer/list/1212/1212
			if re.match(reg,current_url):
				flag = True
				break  #拥有权限可以访问

		if  not flag:
			return HttpResponse("无权访问")   # 这里可以放一个无权访问的html
