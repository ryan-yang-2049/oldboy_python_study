# -*- coding: utf-8 -*-

# __title__ = 'my_middlewares.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.07.09'


from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse
class CustomerMiddleware(MiddlewareMixin):
	def process_request(self,request):
		print("CustomerMiddleware1 process_request .......")
	def process_response(self,request,response):
		print("CustomerMiddleware1 process_response .......")
		return response
	def process_view(self, request, callback, callback_args, callback_kwargs):
		# print("callback1====>",callback)
		# response = callback(request, *callback_args, **callback_kwargs)
		print("CustomerMiddleware1 process_view...")
		# return response
	def process_exception(self,request,exception):
		print("CustomerMiddleware1 process_exception...")
		return HttpResponse("Error: %s" % exception)

class CustomerMiddleware2(MiddlewareMixin):
	def process_request(self,request):
		print("CustomerMiddleware2 process_request .......")
		# return HttpResponse("中断.....")
	def process_response(self,request,response):
		print("CustomerMiddleware2 process_response .......")
		return response
	def process_view(self, request, callback, callback_args, callback_kwargs):
		# print("callback2====>", callback)
		print("CustomerMiddleware2 process_view...")
		# return HttpResponse("123")
	def process_exception(self,request,exception):
		print("CustomerMiddleware2 process_exception...")
		return HttpResponse("Error: %s"%exception)



'''
process_view 如果有返回值的执行顺序(不执行views.py里面的函数)：
	CustomerMiddleware1 process_request .......
	CustomerMiddleware2 process_request .......
	callback1====> <function index at 0x0000020908B55BF8>
	CustomerMiddleware1 process_view...
	callback2====> <function index at 0x0000020908B55BF8>
	CustomerMiddleware2 process_view...
	CustomerMiddleware2 process_response .......
	CustomerMiddleware1 process_response .......

'''