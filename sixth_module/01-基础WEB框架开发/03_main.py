# -*- coding: utf-8 -*-

# __title__ = '03_main.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.06.19'

from wsgiref.simple_server import make_server


def login(environ):
	with open('login.html','rb') as f:
		data = f.read()
	return data

def index(environ):
	with open('index.html','rb') as f:
		data = f.read()
	return data

def fav(environ):
	with open('favicon.ico','rb') as f:
		data = f.read()
	return data





def application(environ, start_response):
	path = environ.get("PATH_INFO")
	start_response('200 OK', [('Content-Type', 'text/html')])
	print(path)
	# 方案一
	# if path == "/favicon.ico":
	# 	with open('favicon.ico','rb') as f:
	# 		data = f.read()
	# 	return [data]
	# elif path == "/login":
	# 	with open("login.html",'rb') as f:
	# 		data = f.read()
	# 	return [data]
	# elif path == "index":
	# 	with open('index.html','rb') as f:
	# 		data = f.read()
	# 	return [data]

	# 方案2:

	url_patterns=[
		("/login",login),
		("/index",index),
		("/favicon.ico",fav)
	]
	func = None
	for item in url_patterns:
		if path == item[0]:
			func = item[1]
			break
			# return  [func()]
		# else:
		# 	return [b'404']

	if func:
		return [func(environ)]
	else:
		return [b'404']

	# return [b"<h1>hello  web</h1>"]


httped=make_server("",8065,application)    # 封装了socket   ,application 是回调函数

# 等待用户连接：conn,addr = sock.accept()
httped.serve_forever()       # application(environ, start_response)









