
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
		当用户请求刚进入时触发执行
		:param request:
		:return:
		"""
		# 1.获取当前用户请求的URL
		# 2.获取当前用户session中保存的权限列表(luffy_permission_url_list_key)（URL）
		# 3.权限信息的匹配

		# 访问：http://127.0.0.1:8000/customer/list/             --path_info 的值为-->  /customer/list/
		# 访问：http://127.0.0.1:8000/customer/list/?id=1&pk=5   --path_info 的值为-->  /customer/list/
		# 访问的URL
		current_url = request.path_info

		# 增加白名单url

		for valid_url in settings.VALID_URL_LIST:
			if re.match(valid_url,current_url):
				# 白名单中的URL无需权限验证即可访问
				return None

		# 获取session信息
		permissions_list = request.session.get(settings.PERMISSION_SESSION_KEY)

		if not permissions_list:
			return HttpResponse('未获取到用户权限信息,请登录！')

		flag = False
		for url in permissions_list:    # 此时的url必须包含起始和终止符，不然，匹配有bug
			reg = "^%s$" % url
			if re.match(reg,current_url):
				flag = True
				break

		if not flag:  # 有权访问
			return HttpResponse("无权访问")













