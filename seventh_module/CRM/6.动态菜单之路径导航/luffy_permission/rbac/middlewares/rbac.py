
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

		# 路径导航列表
		url_record = [
			{'title':'首页','url':'#'}
		]

		for item in permissions_list:    # 此时的url必须包含起始和终止符，不然，匹配有bug
			reg = "^%s$" % item['url']
			if re.match(reg,current_url):
				flag = True
				request.current_selected_permission = item['pid'] or item['id']   # 把权限对应的url传递到inclusion_tag中
				if  not item['pid']:    # 表示的意思是，如果该权限url属于一个菜单权限
					url_record.extend([{'title':item['title'],'url':item['url'],'class':'active'}])
				else:   # 表示该权限不属于菜单权限
					url_record.extend([
						{'title':item['p_title'],'url':item['p_url']},      # 父级菜单的信息
						{'title':item['title'],'url':item['url'],'class':'active'},
					])

				request.breadcrumb = url_record     # 路径导航
				print("request.breadcrumb",request.breadcrumb)

				break
		print("url_record==========>",url_record)
		if not flag:  # 有权访问
			return HttpResponse("无权访问")













