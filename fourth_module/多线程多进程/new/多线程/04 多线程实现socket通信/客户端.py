# -*- coding: utf-8 -*-
"""
__title__ = '客户端.py'
__author__ = 'yangyang'
__mtime__ = '2018.02.06'
"""
import socket
ip_port = ('127.0.0.1',8903)
# from socket import *
# client = socket(AF_INET,SOCK_STREAM)
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ip_port)

while True:
	msg = input(">>:").strip()
	if not msg:continue

	client.send(msg.encode('utf-8'))
	data = client.recv(1024)
	print(data.decode('utf-8'))









