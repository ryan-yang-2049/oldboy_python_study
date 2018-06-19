# -*- coding: utf-8 -*-

# __title__ = 'main.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.06.19'


from wsgiref.simple_server import make_server
from  urls import  url_patterns


def application(environ, start_response):
	path = environ.get("PATH_INFO")
	start_response('200 OK', [('Content-Type', 'text/html')])
	print(path)



	func = None
	for item in url_patterns:
		if path == item[0]:
			func = item[1]
			break


	if func:
		return [func(environ)]
	else:
		return [b'404']

	# return [b"<h1>hello  web</h1>"]


httped=make_server("",8066,application)    # 封装了socket   ,application 是回调函数

# 等待用户连接：conn,addr = sock.accept()
httped.serve_forever()       # applic








