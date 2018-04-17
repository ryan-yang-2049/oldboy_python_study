# -*- coding: utf-8 -*-
"""
__title__ = 'client_main.py'
__author__ = 'yangyang'
__mtime__ = '2018.01.17'
"""

import socket
import struct
import json
import os,sys
import time


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)

from client.conf import settings


class FtpClient(object):
	ADDRESS_FAMILY = socket.AF_INET
	SOCKET_TYPE = socket.SOCK_STREAM
	MAX_PACKET_SIZE = 4096
	PATH_SYMBOL = settings.PATH_SYMBOL

	if os.name == 'posix':
		coding = 'utf-8'
	elif os.name == 'nt':
		coding = 'gbk'


	def __init__(self,server_address,connect=True):
		self.server_address = server_address
		# 创建客户端TCP/IP 的socket套接字对象
		self.client = socket.socket(self.ADDRESS_FAMILY,self.SOCKET_TYPE)

		if connect:
			try:
				self.clinet_connect()
			except:
				self.client_close()
				raise

	def clinet_connect(self):
		# 请求连接服务端
		self.client.connect(self.server_address)

	def client_close(self):
		# 请求断开服务端
		self.client.close()



	def login(self):
		self.user_dict = {}
		while True:
			self.user_dict['username'] = input("login:").strip()
			if len(self.user_dict['username']) == 0:continue
			self.user_dict['password'] = input("password:").strip()
			if len(self.user_dict['password']) == 0: continue

			# 定义客户端用户家目录
			self.user_home_dir = settings.user_home(self.user_dict['username'])
			# 通过socket发送给服务端是发送的bytes类型，因此，先转化成str 在转换成bytes类型
			user_dict_bytes = (json.dumps(self.user_dict)).encode('utf-8')	# bytes类型
			# 发送给服务端
			self.client.send(user_dict_bytes)

			# 接收服务端的消息，经过转换以后，此时的res 是bool 类型 True or False
			res_a = self.client.recv(self.MAX_PACKET_SIZE)
			res_b = json.loads(res_a)
			res = res_b.decode(self.coding)

			# res = json.loads(self.client.recv(self.MAX_PACKET_SIZE))
			print("res:=====>:",res)

			if res:
				print('success')
				'''验证成功 开始执行上传下载等'''
				if hasattr(self,'run'):
					getattr(self,'run')()
			else:
				print("登陆信息错误！")
				self.user_dict.clear()
				continue


	def run(self):

		# 命令操作的字典信息
		cmds_dict ={
			'put':'put_file',
			'get':'get_file',
			'cd' :'remove_dir',
			'ls' :'check_dir',
			'dir':'check_dir',
			'exit':'exit system',
		}
		#链接循环
		while True:
			try:
				inp = input(">>>>:").strip()
				if not inp:continue
				self.client.send(inp.encode(self.coding))
				inp_li = inp.split()
				cmd = inp_li[0]
				if cmd == 'exit':sys.exit()
				if cmd in cmds_dict and hasattr(self,cmds_dict[cmd]):
					getattr(self,cmds_dict[cmd])(inp_li)
			except ConnectionRefusedError:
				break

	def put_file(self,args):
		'''
		用户上传文件到服务端
		args = ['put','filename']
		'''
		filename = r"%s%s%s"%(self.user_home_dir,self.PATH_SYMBOL,args[1])
		if os.path.isfile(filename):
			'''检测是否是文件，有就获取文件内容以及信息等'''
			file_info_dict = settings.file_info(filename)

			#因为发送的bytes类型，因此，要先把字典类型转化成str类型，在从str类型转成bytes类型
			file_info_dict_bytes = (json.dumps(file_info_dict)).encode(self.coding)

			# 先发送报头长度 4
			self.client.send(struct.pack('i',len(file_info_dict_bytes)))

			# 在发送报头，文件信息字典
			self.client.send(file_info_dict_bytes)

			# 发送真实数据
			with open(filename,'rb') as send_file:
				for line in send_file:
					self.client.send(line)
		else:
			print("上传的必须是文件类型")

	def get_file(self,args):
		'''
		客户端从服务端下载文件
		:param args:
		:return:
		'''
		filename = r"%s%s%s"%(self.user_home_dir,self.PATH_SYMBOL,args[1])
		print("客户端文件名",filename)
		#判断文件是否存在：1.不存在
		if not os.path.isfile(filename):
			print("get file")
			# 收取服务端发送的报头长度
			len_header = self.client.recv(4)
			header_size = struct.unpack('i',len_header)[0]

			# 在收取报头:报头就是服务端要发送的字典信息
			header_bytes = self.client.recv(header_size)

			# 从报头中解析出对真实数据的描述信息（将要接收的数据长度）：bytes -->str-->dict
			header_json = header_bytes.decode(self.coding)
			header_dic = json.loads(header_json)
			print(header_dic)
			if isinstance(header_dic,dict):
				total_size = header_dic['file_size']

				# 接收真实的文件内容
				with open(filename,'wb') as recv_file:
					recv_size = 0
					while recv_size < total_size:
						line = self.client.recv(self.MAX_PACKET_SIZE)
						recv_file.write(line)
						recv_size += len(line)
						flag_sign = '#' * int(1.0 * recv_size / total_size * 100)
						spaces = ' '*(100-len(flag_sign))
						sys.stdout.write("\r[%s] %s%%" % (flag_sign + spaces, 100))
						sys.stdout.flush()
						time.sleep(1)
					print('\n')
		else:
			'''
			断点续传：实现思想；
				断点续传就是，在本地已经存在了某一个文件，并且这个文件是在server端文件在传输过程中，中断操作后没有
				能够传输完成的文件,继续上次的位置继续完成。
			实现原理：
				传输文件是一长串的bytes的流式数据的传输，这个数据是有一个长度的bytes。
				首先获取到本地文件的bytes类型的长度。然后用传输过来的bytes 进行切片操作。
				把切片后的内容+上本地内容就是完整的内容。			
			'''

			# 收取服务端发送的报头长度
			len_header = self.client.recv(4)
			header_size = struct.unpack('i',len_header)[0]

			# 在收取报头
			header_bytes = self.client.recv(header_size)

			# 从报头中解析出对真实数据的描述信息
			header_json = header_bytes.decode(self.coding)
			header_dic = json.loads(header_json)

			total_size = header_dic['file_size']
			# filename = header_dic['file_name']

			with open(filename, 'rb+') as recv_file:
				content = recv_file.read()
				content_len = len(content)
				recv_file.seek(content_len)

				recv_size = 0
				while recv_size < total_size:
					line = self.client.recv(1024)
					recv_size += len(line)
					if recv_size >= content_len:
						recv_file.write(line)
						flag_sign = '#' * int(1.0 * recv_size / total_size * 100)
						spaces = ' '*(100-len(flag_sign))
						sys.stdout.write("\r[%s] %s%%" % (flag_sign + spaces, 100))
						sys.stdout.flush()
						time.sleep(1)
				print('\n')

	def check_dir(self,arg):

		len_header = self.client.recv(4)
		header_size = struct.unpack('i', len_header)[0]

		# 再收取报头
		header_bytes = self.client.recv(header_size)

		# 从报头中解析出对真实数据的描述信息
		header_json = header_bytes.decode(self.coding)
		header_dic = json.loads(header_json)

		total_size = header_dic['total_size']

		recv_size = 0
		recv_data = b''
		while recv_size < total_size:
			res = self.client.recv(self.MAX_PACKET_SIZE)
			recv_data += res
			recv_size += len(res)
		print(recv_data.decode(self.coding))




	def remove_dir(self,arg):
		'''
		操作 cd 命令，在客户端不需要去获得是否成功切换了目录，只需要用 ls 去查看返回结果就可以看到是否切换了。
		:return:
		'''
		pass


if __name__ == '__main__':
	IP = '127.0.0.1'
	Port = 8903
	client=FtpClient((IP,Port))
	client.login()























