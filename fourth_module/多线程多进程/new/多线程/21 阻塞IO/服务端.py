# -*- coding: utf-8 -*-
"""
__title__ = 'server_main.py'
__author__ = 'ryan'
__mtime__ = '2018/2/5'
"""
from socket import *
import time
server=socket(AF_INET,SOCK_STREAM)
server.bind(('127.0.0.1',8800))
server.listen(5)
print('starting...')


while True:
	conn,addr=server.accept()
	print(addr)
	while True:
		try:
			data=conn.recv(1024)
			if not data:continue
			conn.send(data.upper())
		except Exception:
			break
	conn.close()
server.close()







