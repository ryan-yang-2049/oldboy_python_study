# -*- coding: utf-8 -*-

# __title__ = 'my_middlewares.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.07.09'


from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
from authDemo import settings
class AuthMiddleware(MiddlewareMixin):
	def process_request(self,request):
		white_list = settings.WHITE_LIST
		if request.path in white_list:
			return None

		if not request.user.is_authenticated:
			return redirect("/login/")











