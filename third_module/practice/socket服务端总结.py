socket 服务端
1.简单版
	1.创建socket套接字对象
	2.绑定ip和端口（元祖类型）
	3.监听挂起的最大连接数
	4.等待客户端连接（bytes类型，需要转换成str类型）
	5.接收客户端的数据
	6.返回数据可客户端（转换成bytes类型）
	7.关闭客户端连接
	8.关闭socket的套接字对象


2.服务端模拟ssh登陆
import subprocess,socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('127.0.0.1',9900))
server.listen(5)

while True:
	conn,client_addr = server.accept()
	
	while True:
		try:
			cmd = conn.recv(1024)
			if not cmd:break
			res = subprocess.Popen(cmd.decode('utf-8'),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
			
			stdout = res.stdout.read()
			stderr = res.stderr.read()
			
			conn.send(stdout+stderr)
		except ConnectionResetError:
			break
		
	conn.close()
	
server.close()




3.终极版ssh客户端（解决粘包问题）
import os
import socket
import struct
import json

if os.name = 'posix':
	coding='utf-8'
elif os.name = 'nt':
	coding='gbk'

ip_port = ('127.0.0.1',8099)
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ip_port)
server.listen(5)

while True:
	conn,client_addr = server.accept()
	while True:
		try:
			cmd = conn.recv(8096)
			if not cmd:continue
			
			res = subprocess.Popen(cmd.decode(coding),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
			
			stdout=res.stdout.read()
			stderr=res.stderr.read()
			
			res_dic = {'total_size':len(stdout)+len(stderr)}
			
			res_json = json.dumps(res_dic)
			
			res_bytes = res_json.encode(coding)
			
			conn.send(struct.pack('i',len(res_bytes))
			
			conn.send(res_bytes)
			
			conn.send(stdout)
			conn.send(stderr)
			
		except ConnectionResetError:
			break
	conn.close()
server.close()
			
			
	


































