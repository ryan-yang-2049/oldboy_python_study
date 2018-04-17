socket 客户端
1.简单版
	1.创建客户端socket对象
	2.连接到服务端
	3.发送消息给服务端
	4.接收服务端的数据 （bytes类型，需要转换成str类型）
	5.关闭客户端的socket套接字对象





2.客户端模拟ssh登陆

	client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	client.connect(('127.0.0.1',9900))
	
	while True:
		cmd = input(">>:").strip()
		if cmd == 'exit':break
		if not cmd:continue
		client.send(cmd.decode('utf-8'))
		
		data = client.recv(1024)
		print(data.decode('utf-8'))
	client.close()




3.终极版ssh服务端（解决粘包问题）
import os
import socket
import struct
import json

if os.name = 'posix':
	coding='utf-8'
elif os.name = 'nt':
	coding='gbk'

ip_port = ('127.0.0.1',8099)
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ip_port)

while True:
	cmd = input('>>:')
	if not cmd :continue
	client.send(cmd.encode(coding))
	
	recv_res = client.recv(4)
	header_size = struct.unpack('i',recv_res)[0]
	
	header_types = client.recv(header_size)
	
	header_json = header_types.decode(coding)
	
	header_dic = json.loads(header_json)
	
	taotal_size = header_dic['total_size']
	
	recv_size = 0
	recv_data = b''
	while recv_size < total_size:
		res = client.recv(1024)
		recv_data += res
		recv_size += len(res)
	print(recv_data.decode(coding))
client.close()




































