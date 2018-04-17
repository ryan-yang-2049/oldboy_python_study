# -*- coding: utf-8 -*-
"""
__title__ = 'server_main.py'
__author__ = 'ryan'
__mtime__ = '2018/2/5'
"""
from socket import *
import time
import select


server=socket(AF_INET,SOCK_STREAM)
server.bind(('127.0.0.1',8800))
server.listen(5)
server.setblocking(False)
print('starting...')
reads_l = [server,]

while True:
	r_l,_,_ = select.select(reads_l,[],[])
	print(r_l)
	for obj in r_l:
		if obj == server:
			conn,addr = obj.accept()
			reads_l.append(conn)
			print(addr)
		else:
			try:
				data = obj.recv(1024)
				obj.send(data.upper())
			except ConnectionResetError:
				pass






