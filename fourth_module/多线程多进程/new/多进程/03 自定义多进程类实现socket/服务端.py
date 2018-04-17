# -*- coding: utf-8 -*-
"""
__title__ = 'server_main.py'
__author__ = 'yangyang'
__mtime__ = '2018.02.06'
"""
import socket
from multiprocessing import Process

# class MyProcess(Process):
# 	def __init__(self):
# 		super().__init__()
#
# 	def run(self):
# 		pass

class MySocket(object):
	ADDRESS_FAMILY = socket.AF_INET
	SOCKET_TYPE = socket.SOCK_STREAM
	ALLOW_REUSE_ADDRESS = False
	MAX_PACKET_SIZE = 4096

	REQUEST_QUEUE_SIZE = 5
	def __init__(self,server_address,bind_and_active=True):
		self.server_addresss = server_address

		if bind_and_active:
			try:
				self.create_socket()
			except:
				self.server_close()
				raise


	def create_socket(self):
		self.server = socket.socket(self.ADDRESS_FAMILY,self.SOCKET_TYPE)
		self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.server.bind(self.server_addresss)
		self.server.listen(self.REQUEST_QUEUE_SIZE)

	def server_close(self):
		self.server.close()



	def connect(self):
		while True:
			conn,client_addr = self.server.accept()

			p = Process(target=self.communication,kwargs={"conn":conn,"client_addr":client_addr})
			p.start()


	def communication(self,conn,client_addr):
		while True:
			try:
				print("conn:%s" % conn)
				print("client_addr: " ,client_addr)
				res = conn.recv(self.MAX_PACKET_SIZE)
				if not res:continue
				conn.send(res.upper())
			except ConnectionResetError:
				break


if __name__ == '__main__':
	ip_port = ('127.0.0.1', 8092)
	obj = MySocket(ip_port)
	obj.connect()

