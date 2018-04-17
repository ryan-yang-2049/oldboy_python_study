# -*- coding: utf-8 -*-
"""
__title__ = 'server_main.py'
__author__ = 'yangyang'
__mtime__ = '2018.02.11'
"""
import os,sys
import socket
import json
import struct
import time
import subprocess
import queue
from threading import Thread,currentThread
from  concurrent.futures import ThreadPoolExecutor

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)

from server.conf import settings


class FtpServer(object):
	ADDRESS_FAMILY = socket.AF_INET
	SOCKET_TYPE = socket.SOCK_STREAM
	ALLOW_REUSE_ADDRESS = False
	MAX_PACKET_SIZE = 4096
	coding = settings.coding
	PATH_SYMBOL = settings.PATH_SYMBOL
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
		self.pool = ThreadPoolExecutor(10)
		while True:
			conn,client_addr = self.server.accept()
			t = self.pool.submit(self.login_info_auth,conn)

	def login_info_auth(self,conn):
		while True:
			try:
				res = conn.recv(1024)
				self.user_dict = json.loads((res).decode(self.coding))
				self.user_name = self.user_dict['username']
				self.password = self.user_dict['password']

				# 用于cd操作时接收用户的切换目录的变量: dir_li
				self.dir_li = [settings.user_home(self.user_name), ]

				# 用户当前的绝对路径
				self.absolute_dir = [settings.user_home(self.user_name), ]
				# 用户的家目录
				self.user_home = settings.user_home(self.user_name)

				# 用户的额度
				# self.uesr_quota = int(settings.user_disk_quota(self.user_home))

				# 验证用户信息，及磁盘额度大小
				login_res = settings.UserManage(self.user_name, self.password)
				return_res = login_res.auth_user()  # True or False bool 类型
				# self.disk_quota = int(login_res.check_user_quota())
				return_res_bytes = (json.dumps(return_res)).encode('utf-8')
				print("return_res_bytes:",return_res_bytes)
				if return_res and hasattr(self, 'run'):
					conn.send(return_res_bytes)
					getattr(self, 'run')(conn)
				else:
					conn.send(return_res_bytes)
					continue

			except BlockingIOError:
				continue
			except Exception:
				conn.close()
				break
	def run(self,conn):

		# self.message[conn] = queue.Queue()
		cmds_dict ={
			'put':'put_file',
			'get':'get_file',
			'cd' :'remove_dir',
			'ls' :'check_dir',
			'dir':'check_dir',
			'pwd':'this_directory',
		}
		while True:
			try:
				cmd_res = conn.recv(self.MAX_PACKET_SIZE)
				if not cmd_res:break
				cmd = (cmd_res.decode(self.coding)).split()
				if cmd[0] in cmds_dict and hasattr(self,cmds_dict[cmd[0]]):
					execute_func = getattr(self,cmds_dict[cmd[0]])
					execute_func(cmd,conn)
			except ConnectionRefusedError:
				break

	def get_file(self,cmds,conn):
		'''
		用于客户端下载文件
		客户端下载，就是服务端上传
		'''
		# 检查磁盘额度

		# 上传后的文件应该是用户切换后的当前目录下的文件
		dirname = (self.PATH_SYMBOL).join(self.dir_li)
		filename = "%s%s%s"%(dirname,self.PATH_SYMBOL,cmds[1])
		if os.path.isfile(filename):
			file_info_dict = settings.file_info(filename)

			# 发送 bytes 类型给客户端	(str).encode(utf-8) -->bytes
			file_info_dict_bytes = (json.dumps(file_info_dict)).encode(self.coding)

			# 先发送报头的长度
			conn.send(struct.pack('i',len(file_info_dict_bytes)))

			# 在发送报头，文件信息字典的内容
			conn.send(file_info_dict_bytes)

			# 在发送真实数据
			with open(filename,'rb') as send_file:
				for line in send_file:
					conn.send(line)
		else:
			# print("文件不存在")
			return_info = "文件不存在!"

			return_info_bytes = return_info.encode(self.coding)

			conn.send(struct.pack('i',len(return_info_bytes)))

			conn.send(return_info_bytes)

	def put_file(self,cmds,conn):
		'''客户端上传就是服务端获取，因此 服务端就是get file'''
		dirname = (self.PATH_SYMBOL).join(self.dir_li)
		filename = "%s%s%s"%(dirname,self.PATH_SYMBOL,cmds[1])
		if not os.path.exists(filename):
			# 先收取报头的长度
			len_header = conn.recv(4)
			header_size = struct.unpack('i',len_header)[0]

			# 再收取报头
			header_bytes = conn.recv(header_size)

			# 从报头中解析出对真实数据的描述信息
			header_json = header_bytes.decode(self.coding)
			header_dic = json.loads(header_json)

			total_size = header_dic['file_size']
			# filename = header_dic['file_name']

			with open(filename,'wb') as recv_file:
				recv_size = 0
				while recv_size < total_size:
					line = conn.recv(4096)
					recv_file.write(line)
					recv_size += len(line)
					flag_sign = '#' * int(1.0 * recv_size / total_size * 100)
					spaces = ' '*(100-len(flag_sign))
					sys.stdout.write("\r[%s] %s%%" % (flag_sign + spaces, 100))
					sys.stdout.flush()
					time.sleep(1)
				print('\n')
		else:
			os.remove(filename)

	def file_info(self,filename):
		self.file_info_dict = {}
		if os.path.exists(filename) and os.path.isfile(filename):
			self.file_info_dict['file_md5'] = settings.getfilemd5(filename)
			self.file_info_dict['file_size'] = os.path.getsize(filename)
			self.file_info_dict['file_name'] = filename
			return self.file_info_dict
		else:
			return False


	def remove_dir(self,cmds,conn):
		'''
		用户不能查看当前目录的路径
		cd 操作有以下情况：
		1. cd  这样的情况就直接切到 用户更目录 user_home/
		2. cd .. 那就删除 列表里面的最后一个元素，只有一个家目录的时候 就不在
		3. cd dir1 那就添加到列表里面，并进行判断，如果系统有这个目录，那就返回这个路径，没有，那么久返回错误
		:param arg:
		:return:
		'''
		if len(cmds) == 2:
			switch_dir = cmds[1]
			if switch_dir == '..':
				if len(self.dir_li) == 2:
					self.dir_li = [settings.user_home(self.user_name),]
				else:
					self.dir_li.pop()

			elif len(switch_dir) > 0:
				self.dir_li.append(switch_dir)
		if len(cmds) == 1:
			self.dir_li = [settings.user_home(self.user_name),]

	def check_dir(self,arg,conn):
		'''
		用户查看文件 [ls,]
		:return:
		'''
		cmd = arg[0]
		if os.name == 'posix':
			cmd = 'ls'
		elif os.name == 'nt':
			cmd = 'dir'

		dirname = (self.PATH_SYMBOL).join(self.dir_li)
		if os.path.exists(dirname):
			obj = subprocess.Popen("%s %s"%(cmd,dirname),shell=True,
								   stdout=subprocess.PIPE,
								   stderr=subprocess.PIPE)

			stdout = obj.stdout.read()
			stderr = obj.stdout.read()
			cmd_dic = {'total_size':len(stdout)+len(stderr)}
			header_json = json.dumps(cmd_dic)
			header_bytes = header_json.encode(self.coding)
			conn.send(struct.pack('i',len(header_bytes)))
			conn.send(header_bytes)
			conn.send(stdout)
			conn.send(stderr)
		else:
			stdout = "dirname not exist"
			stderr = " "
			cmd_dic = {'total_size':len(stdout)+len(stderr)}
			header_json = json.dumps(cmd_dic)
			header_bytes = header_json.encode(self.coding)
			conn.send(struct.pack('i',len(header_bytes)))
			conn.send(header_bytes)
			conn.send(stdout)
			conn.send(stderr)

if __name__ == '__main__':
	ip_port = ('127.0.0.1',8903)
	obj = FtpServer(ip_port)
	obj.connect()

