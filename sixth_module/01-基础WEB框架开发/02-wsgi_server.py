# -*- coding: utf-8 -*-

# __title__ = '02-wsgi_server.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.06.19'

from wsgiref.simple_server import make_server

def application(environ, start_response):
	# 按照http协议解析数据  environ
	# 按照http协议进行组装数据 start_response

	# print(environ.get("PATH_INFO"))
	# print(type(environ))
	# 200 ok  响应首行

	# 当前请求路径
	path = environ.get("PATH_INFO")
	start_response('200 OK', [])
	print(path)

	if path=="/login":
		with open("login.html",'r',encoding='UTF-8') as f:
			data = f.read()
			# print("===>",type(data))
			return [data.encode('utf8')]
	elif path=="/index":
		with open("index.html",'r',encoding='UTF-8') as f:
			data = f.read()
			# print("===>", type(data))
			return [data.encode('utf8')]
	elif path == "/favicon.ico":
		with open('favicon.ico','rb') as f:
			data = f.read()
		return [data]

	# return [b"<h1>hello  web</h1>"]        # 返回必须是劣列表，wsgi的要求

httped=make_server("",8064,application)    # 封装了socket   ,application 是回调函数

# 等待用户连接：conn,addr = sock.accept()
httped.serve_forever()       # application(environ, start_response)








