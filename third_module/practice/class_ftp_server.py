# -*- coding: utf-8 -*-
"""
__title__ = 'class_ftp_server.py'
__author__ = 'yangyang'
__mtime__ = '2018.01.24'
"""
import  os,socket,struct,json,subprocess

class FtpServer(object):
	ADDRESS_FAMILY = socket.AF_INET
	SOCKET_TYPE = socket.SOCK_STREAM
	MAX_PACKET_SIZE = 8192
	if os.name == 'posix':
		coding = 'utf-8'
	else:
		coding = 'gbk'

	REQUEST_QUEUE_SIZE = 5

	def __init__(self,server_address,connect=True):
		self.server_address = server_address
		self.server = socket.socket(self.ADDRESS_FAMILY,self.SOCKET_TYPE)

		if connect:
			try:
				self.server_connect()
				self.run()
			except:
				self.server_close()
				raise

	def server_connect(self):
		self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.server.bind(self.server_address)
		self.server.listen(self.REQUEST_QUEUE_SIZE)

	def server_close(self):
		self.server.close()

	def run(self):
		while True:
			self.conn,self.client_addr = self.server.accept()
			print(self.conn)
			while True:
				try:
					cmd = self.conn.recv(self.MAX_PACKET_SIZE)
					if not cmd:continue
					res = subprocess.Popen(cmd.decode(self.coding),shell=True,
					                       stdout=subprocess.PIPE,
					                       stderr=subprocess.PIPE)
					stdout = res.stdout.read()
					stderr = res.stderr.read()

					res_dic = {'total_size':len(stdout)+len(stderr)}

					res_json = json.dumps(res_dic)

					res_bytes = res_json.encode(self.coding)

					self.conn.send(struct.pack('i',len(res_bytes)))
					self.conn.send(res_bytes)

					self.conn.send(stdout)
					self.conn.send(stderr)
				except ConnectionResetError:
					break
			self.conn.close()

obj = FtpServer(('127.0.0.1', 9999))
obj.run()