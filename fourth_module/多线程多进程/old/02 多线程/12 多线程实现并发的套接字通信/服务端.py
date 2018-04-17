#coding:utf-8

'''
可以考虑是否同一时刻只能运行多少个线程的限制
'''

import  socket
from threading import Thread

def communicate(conn):
	while True:
		try:
			data = conn.recv(104)
			if not data:break
			conn.send(data.upper())
		except ConnectionResetError:
			break
	conn.close()

def server(ip_port):
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind(ip_port)
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
	server.listen(5)
	while True:
		conn,client_addr = server.accept()
		t=Thread(target=communicate,args=(conn,))
		t.start()
	server.close()

if __name__ == '__main__':
	ip_port = ('127.0.0.1',8081)
	server(ip_port)