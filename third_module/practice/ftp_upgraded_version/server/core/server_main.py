# -*- coding: utf-8 -*-
"""
__title__ = 'servr_main.py'
__author__ = 'yangyang'
__mtime__ = '2018.01.16'
"""

'''
ftp 的服务端实现方法
'''
import os,sys
import hashlib
import socket
import json
import struct
import time
import subprocess

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from server.conf import settings



class FtpServer(object):

	ADDRESS_FAMILY = socket.AF_INET
	SOCKET_TYPE = socket.SOCK_STREAM
	ALLOW_REUSE_ADDRESS = False
	MAX_PACKET_SIZE = 8192
	if os.name == 'posix':
		coding = 'utf-8'
		PATH_SYMBOL = '/'
	elif os.name == 'nt':
		coding = 'gbk'
		PATH_SYMBOL = '%s'%('\\')

	REQUEST_QUEUE_SIZE = 5
	server_dir = settings.user_home_dir

	# 固定家目录的上级目录
	fixed_home_dir = [settings.user_home_dir,]
	# 用于用户cd操作时，接收的用户cd的路径名，可以进行拼接获取到cd 的地址。
	dir_li = [settings.user_home_dir,]


	def __init__(self,server_address,bind_and_activate=True):
		self.server_address =server_address
		self.socket = socket.socket(self.ADDRESS_FAMILY,self.SOCKET_TYPE)

		if bind_and_activate:
			try:
				self.server_bind()			# 绑定地址
				self.server_activate()		# 服务端监听的最大挂起链接数
			except:
				self.server_close()
				raise

	def server_bind(self):
		'''
		绑定服务端自己的地址
		:return:
		'''
		if not self.ALLOW_REUSE_ADDRESS:
			''' #防止程序出现（OSError: [Errno 98] Address already in use）'''
			self.socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
		self.socket.bind(self.server_address)
		self.server_address = self.socket.getsockname()	# 当前套接字的地址 ('127.0.0.1', 8081)

	def server_activate(self):
		'''
		开始TCP监听，以及挂起的最大连接数
		:return:
		'''
		self.socket.listen(self.REQUEST_QUEUE_SIZE)

	def server_close(self):
		'''
		关闭服务端
		:return:
		'''
		self.socket.close()

	def get_request(self):
		# 接收客户端消息
		return self.socket.accept()

	def close_request(self,request):
		request.close()

	def login_auth(self):
		'''
		客户端登陆时，在服务端的配置文件里面验证用户名和密码
		:return:
		'''
		while True:
			self.conn,self.client_addr = self.get_request()
			while True:
				self.res = self.conn.recv(1024)

				# 这里如果是break 那么就需要客户端重新链接，并且服务端会关闭。
				if not self.res:continue
				self.user_dict = json.loads((self.res).decode(self.coding))
				self.user_name = self.user_dict['username']
				self.password = self.user_dict['password']
				# self.disk_quota = self.user_dict['disk_quota']

				#定义用户当前目录列表
				self.dir_li.append(self.user_name)	# 需要进行拼接的字典
				# 用户当前的绝对路径
				self.absolute_dir = (self.PATH_SYMBOL).join(self.dir_li)

				self.fixed_home_dir.append(self.user_name)	# 用户的真正的家目录
				self.user_home = (self.PATH_SYMBOL).join(self.fixed_home_dir)

				#用户的额度
				# self.uesr_quota = int(settings.user_disk_quota(self.user_home))

				# 验证用户信息，及磁盘额度大小
				login_res = settings.UserManage(self.user_name,self.password)
				return_res = login_res.auth_user()	# True or False bool 类型
				self.disk_quota = int(login_res.check_user_quota())

				if return_res and hasattr(self,'run'):
					return_res_bytes = (json.dumps(return_res)).encode('utf-8')		# 给客户端返回登陆状态
					self.conn.send(return_res_bytes)
					execute_func = getattr(self,'run')
					execute_func()
			else:
				break
			self.conn.close()

	def run(self):
		cmds_dict ={
			'put':'get_file',
			'get':'put_file',
			'cd' :'remove_dir',
			'ls' :'check_dir',
			'dir':'check_dir',
			'pwd':'this_directory',
			'exit':'exit process',
		}
		while True:
			try:
				cmd_res = self.conn.recv(self.MAX_PACKET_SIZE)
				if not cmd_res:break
				cmd = cmd_res.decode(self.coding).split()
				if cmd[0] == 'exit':
					sys.exit()
				if cmd[0] in cmds_dict and hasattr(self,cmds_dict[cmd[0]]):
					print("开始执行方法")
					execute_func = getattr(self,cmds_dict[cmd[0]])
					execute_func(cmd)
			except ConnectionRefusedError:
				break

	def put_file(self,cmds):
		'''
		用于客户端下载文件
		客户端下载，就是服务端上传
		'''
		# 检查磁盘额度

		print("put_file")
		# 上传后的文件应该是用户切换后的当前目录下的文件
		filename = "%s%s%s"%(self.absolute_dir,self.PATH_SYMBOL,cmds[1])

		# self.user_server_home_dir = (self.PATH_SYMBOL).join(self.fixed_home_dir)
		# self.user_get_file = "%s%s%s"%(self.dir_li,self.PATH_SYMBOL,filename)
		if os.path.isfile(filename):
			file_info_dict = settings.file_info(filename)

			# 发送 bytes 类型给客户端	(str).encode(utf-8) -->bytes
			file_info_dict_bytes = (json.dumps(file_info_dict)).encode(self.coding)

			# 先发送报头的长度
			self.conn.send(struct.pack('i',len(file_info_dict_bytes)))

			# 在发送报头，文件信息字典的内容
			self.conn.send(file_info_dict_bytes)

			# 在发送真实数据
			with open(filename,'rb') as send_file:
				for line in send_file:
					self.conn.send(line)
		else:
			# print("文件不存在")
			return_info = "文件不存在!"

			return_info_bytes = return_info.encode(self.coding)

			self.conn.send(struct.pack('i',len(return_info_bytes)))

			self.conn.send(return_info_bytes)

	def get_file(self,cmds):
		'''客户端上传就是服务端获取，因此 服务端就是get file'''

		filename = "%s%s%s" % (self.absolute_dir, self.PATH_SYMBOL, cmds[1])
		# self.user_server_home_dir = (self.PATH_SYMBOL).join(self.fixed_home_dir)
		# self.user_server_home = "%s%s%s"%(self.user_server_home_dir,self.PATH_SYMBOL,filename)
		while True:
			if not os.path.exists(filename):


				# 先收取报头的长度
				len_header = self.conn.recv(4)
				header_size = struct.unpack('i',len_header)[0]

				# 再收取报头
				header_bytes = self.conn.recv(header_size)

				# 从报头中解析出对真实数据的描述信息
				header_json = header_bytes.decode(self.coding)
				header_dic = json.loads(header_json)

				total_size = header_dic['file_size']
				filename = header_dic['file_name']
				if self.disk_quota < 10:
					break
				else:
					# 接收真实的文件内容
					with open(filename,'wb') as recv_file:
						recv_size = 0
						while recv_size < total_size:
							line = self.conn.recv(4096)
							recv_file.write(line)
							recv_size += len(line)
							flag_sign = '#' * int(1.0 * recv_size / total_size * 100)
							spaces = ' '*(100-len(flag_sign))
							sys.stdout.write("\r[%s] %s%%" % (flag_sign + spaces, 100))
							sys.stdout.flush()
							time.sleep(1)
						print('\n')
				break

			else:
				os.remove(filename)
				continue

	def file_info(self,filename):
		self.file_info_dict = {}
		if os.path.exists(filename) and os.path.isfile(filename):
			self.file_info_dict['file_md5'] = settings.getfilemd5(filename)
			self.file_info_dict['file_size'] = os.path.getsize(filename)
			self.file_info_dict['file_name'] = filename
			return self.file_info_dict
		else:
			return False


	def remove_dir(self,cmds):
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
					self.dir_li = self.fixed_home_dir
				else:
					self.dir_li.pop()

			elif len(switch_dir) > 0:
				self.dir_li.append(switch_dir)
		if len(cmds) == 1:
			self.dir_li = self.fixed_home_dir

	def check_dir(self,arg):
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
			self.conn.send(struct.pack('i',len(header_bytes)))
			self.conn.send(header_bytes)
			self.conn.send(stdout)
			self.conn.send(stderr)
		else:
			stdout = "dirname not exist"
			stderr = " "
			cmd_dic = {'total_size':len(stdout)+len(stderr)}
			header_json = json.dumps(cmd_dic)
			header_bytes = header_json.encode(self.coding)
			self.conn.send(struct.pack('i',len(header_bytes)))
			self.conn.send(header_bytes)
			self.conn.send(stdout)
			self.conn.send(stderr)


