# -*- coding: utf-8 -*-
import re
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse
from django.conf import settings


class RbacMiddleware(MiddlewareMixin):
	"""
	用户权限信息校验
	"""

	def process_request(self, request):
		"""
		当用户请求进入时触发执行
		:param request:
		:return:
		"""
		"""
		1.获取当前用户请求URL
		2.获取当前用户在session中保存的权限列表 
		3.权限信息的匹配
		"""

		current_url = request.path_info

		for valid_url in settings.VALID_URL_LIST:
			if re.match(valid_url, current_url):
				return None  # 表示中间件不拦截，直接执行试图里面的内容

		permission_dict = request.session.get(settings.PERMISSION_SESSION_KEY)

		if not permission_dict:
			return HttpResponse('为获取到用户权限信息，请登录!')

		flag = False  # Flag=False 的时候表示未匹配成功

		url_record = [
			{'title':'首页','url':'/index/'}
		]

		for item in permission_dict.values():
			reg = "^%s$" % (item['url'])
			if re.match(reg, current_url):
				flag = True
				request.current_selected_permission = item['pid'] or item['id']  # 第19课
				print("middle:",request.current_selected_permission)

				if not item['pid']:
					url_record.extend([{'title':item['title'],'url':item['url'],'class':'active success'}])
				else:
					url_record.extend([
						{'title':item['p_title'],'url':item['p_url']},
						{'title': item['title'], 'url': item['url'],'class':'active success'}
					])
				request.breadcrumb = url_record
				break

		if not flag:
			return HttpResponse("无权访问!")
