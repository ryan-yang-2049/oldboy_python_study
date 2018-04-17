# -*- coding: utf-8 -*-
"""
__title__ = 'class_ftp_client.py'
__author__ = 'yangyang'
__mtime__ = '2018.01.24'
"""
import os
import json
import socket
import struct

class FtpClient(object):
	ADDRESS_FAMILY = socket.AF_INET
	SOCKET_TYPE = socket.SOCK_STREAM
	MAX_PACKET_SIZE = 8192
	if os.name == 'posix':
		coding = 'utf-8'
	elif os.name == 'nt':
		coding = 'gbk'

	def __init__(self,server_address,connect=True):
		self.server_address = server_address
		self.client = socket.socket(self.ADDRESS_FAMILY,self.SOCKET_TYPE)
		if connect:
			try:
				self.client_connect()
			except:
				self.client_close()
				raise

	def client_connect(self):
		self.client.connect(self.server_address)

	def client_close(self):
		self.client.close()

	def run(self):
		while True:
			cmd = input(">>:").strip()
			if not cmd:continue
			# 发送命令执行结果
			self.client.send(cmd.encode(self.coding))

			# 接收服务端的返回结果
			res = self.client.recv(4)
			header_size = struct.unpack('i',res)[0]

			header_types = self.client.recv(header_size)

			header_json = header_types.decode(self.coding)

			header_dic = json.loads(header_json)

			total_size = header_dic['total_size']

			recv_size = 0
			recv_data = b''

			while recv_size < total_size:
				res=self.client.recv(1024)
				recv_data += res
				recv_size += len(res)
			print(recv_data.decode(self.coding))

obj = FtpClient(('127.0.0.1',9999))
obj.run()