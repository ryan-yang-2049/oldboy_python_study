# -*- coding: utf-8 -*-
"""
__title__ = '01-JDserver.py'
__author__ = 'ryan'
__mtime__ = '2018/6/17'
"""

import  socket

sock = socket.socket()
sock.bind(("127.0.0.1",8801))
sock.listen(5)

while True:
	# conn 客户端套接字
	conn,addr = sock.accept()

	data = conn.recv(1024)
	print("data:",data)
	# HTTP/1.1 200 OK  相应首行
	# 读取html文件
	# POST 请求才有请求头数据

	# 按照http请求协议解析数据

	# 专注于web业务开发

	# 按照http响应协议封装数据




	with open('login.html','r') as f:
		data = f.read()
	conn.send(("HTTP/1.1 200 OK\r\n\r\n%s"%data).encode('utf8'))
	conn.close()






