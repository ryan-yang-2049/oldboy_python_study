# -*- coding: utf-8 -*-
"""
__title__ = '多进程服务端.py'
__author__ = 'yangyang'
__mtime__ = '2018.01.29'
"""
import  socket
from multiprocessing import  Process

def talk(conn):
	while True:
		try:
			res = conn.recv(1024)
			if not res:continue
			conn.send(res)
		except ConnectionResetError:
			break
	conn.close()



def server(ip_port):
	server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server.bind(ip_port)
	server.listen(5)

	while True:
		conn, client_addr = server.accept()
		p = Process(target=talk, args=(conn,))
		p.start()

	server.close()



if __name__ == '__main__':
	ip_port = ('127.0.0.1',8082)
	server(ip_port)


