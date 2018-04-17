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

from conf import settings

def getfilemd5(filename):
	filemd5 = None
	if os.path.isfile(filename):
		f = open(filename,'rb')
		md5_obj = hashlib.md5()
		while True:
			data = f.read(102400)
			if not data:break
			md5_obj.update(data)
		hash_code = md5_obj.hexdigest()
		f.close()
		filemd5 = str(hash_code).lower()
	return filemd5

class FtpServer(object):

	address_family = socket.AF_INET
	socket_type = socket.SOCK_STREAM
	allow_reuse_address = False
	max_packet_size = 8192
	if os.name == 'posix':
		coding = 'utf-8'
		path_symbol = '/'
	elif os.name == 'nt':
		coding = 'gbk'
		path_symbol = '%s'%('\\')

	request_queue_size = 5
	server_dir = settings.user_home_dir

	#用于cd 切换目录用的列表
	fixed_home_dir = [settings.user_home_dir,]
	#用于添加目录
	dir_li = [settings.user_home_dir,]
	def __init__(self,server_address,bind_and_activate=True):
		self.server_address =server_address
		self.socket = socket.socket(self.address_family,self.socket_type)

		if bind_and_activate:
			try:
				self.server_bind()
				self.server_activate()
			except:
				self.server_close()
				raise

	def server_bind(self):
		if not self.allow_reuse_address:
			''' #防止程序出现（OSError: [Errno 98] Address already in use）'''
			self.socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
		self.socket.bind(self.server_address)
		self.server_address = self.socket.getsockname()	# 当前套接字的地址

	def server_activate(self):
		'''
		开始TCP监听，以及挂起的最大连接数
		:return:
		'''
		self.socket.listen(self.request_queue_size)

	def server_close(self):
		self.socket.close()

	def get_request(self):
		return self.socket.accept()

	def close_request(self,request):
		request.close()

	def login_auth(self):
		while True:
			self.conn,self.client_addr = self.get_request()
			while True:
				self.res = self.conn.recv(1024)
				if not self.res:continue
				self.user_dict = json.loads(self.res.decode(self.coding))
				self.user_name = self.user_dict['username']
				self.password = self.user_dict['password']

				#定义用户家目录
				self.dir_li.append(self.user_name)
				self.fixed_home_dir.append(self.user_name)

				login_res = settings.UserManage(self.user_name,self.password)
				return_res = login_res.auth_user()
				return_res_bytes = (json.dumps(return_res)).encode('utf-8')
				self.conn.send(return_res_bytes)
				if return_res and hasattr(self,'run'):
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
				cmd_res = self.conn.recv(self.max_packet_size)
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

	# def get_filename(self,filename):
	# 	if os.name == 'posix':  # linux or mac
	# 		pass
	# 	# windows
	# 	elif os.name == 'nt':
	# 		self.user_server_home = r"%s%s\%s" % (self.server_dir, self.user_dict['username'],filename)

	def put_file(self,arg):
		print("put_file")
		cmd_li = arg
		filename = cmd_li[1]
		self.user_server_home_dir = (self.path_symbol).join(self.fixed_home_dir)
		self.user_server_home = "%s%s%s"%(self.user_server_home_dir,self.path_symbol,filename)
		if os.path.isfile(self.user_server_home):
			file_info_dict = settings.file_info(self.user_server_home)

			# 发送 bytes 类型给客户端	(str).encode(utf-8) -->bytes
			file_info_dict_bytes = (json.dumps(file_info_dict)).encode(self.coding)

			# 先发送报头的长度
			self.conn.send(struct.pack('i',len(file_info_dict_bytes)))

			# 在发送报头，文件信息字典的内容
			self.conn.send(file_info_dict_bytes)

			# 在发送真实数据
			with open(self.user_server_home,'rb') as send_file:
				for line in send_file:
					self.conn.send(line)
		else:
			# print("文件不存在")
			return False

	def get_file(self,arg):
		'''客户端上传就是服务端获取，因此 服务端就是get file'''
		cmd_li = arg
		filename = cmd_li[1]
		self.user_server_home_dir = (self.path_symbol).join(self.fixed_home_dir)
		self.user_server_home = "%s%s%s"%(self.user_server_home_dir,self.path_symbol,filename)
		while True:
			if not os.path.isfile(self.user_server_home):

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

				# 接收真实的文件内容
				with open(self.user_server_home,'wb') as recv_file:
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
				os.remove(self.user_server_home)
				continue

	def file_info(self,filename):
		self.file_info_dict = {}
		if os.path.exists(filename) and os.path.isfile(filename):
			self.file_info_dict['file_md5'] = getfilemd5(filename)
			self.file_info_dict['file_size'] = os.path.getsize(filename)
			self.file_info_dict['file_name'] = filename
			return self.file_info_dict
		else:
			return False

	def get_user_homedir(self):
		'''
		用户家目录
		:return:
		'''
		if os.name == 'posix':  # linux or mac
			self.user_home = "%s%s/" % (self.server_dir, self.user_dict['username'])
		# windows
		elif os.name == 'nt':
			self.user_home = r"%s%s\\" % (self.server_dir, self.user_dict['username'])



	def remove_dir(self,arg):
		'''
		用户不能查看当前目录的路径
		cd 操作有以下情况：
		1. cd  这样的情况就直接切到 用户更目录 user_home/
		2. cd .. 那就删除 列表里面的最后一个元素，只有一个家目录的时候 就不在
		3. cd dir1 那就添加到列表里面，并进行判断，如果系统有这个目录，那就返回这个路径，没有，那么久返回错误
		:param arg:
		:return:
		'''
		cmd_li = arg
		if len(cmd_li) == 2:
			switch_dir = arg[1]
			if switch_dir == '..':
				if len(self.dir_li) == 2:
					self.dir_li = self.fixed_home_dir
				else:
					self.dir_li.pop()

			elif len(switch_dir) > 0:
				self.dir_li.append(switch_dir)
		if len(cmd_li) == 1:
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

		dirname = (self.path_symbol).join(self.dir_li)
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


