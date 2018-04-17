'''
__title__ = ''
__author__ = 'ryan'
__mtime__ = '2018/1/16'
ssh ftp 客户端
'''

import os
import socket
import struct
import json

if os.name == 'posix':
	coding = 'utf-8'
elif os.name == 'nt':
	coding = 'gbk'

ip_port = ('127.0.0.1', 8099)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ip_port)

while True:
	cmd = input('>>:')
	if not cmd: continue
	client.send(cmd.encode(coding))

	recv_res = client.recv(4)
	header_size = struct.unpack('i', recv_res)[0]

	header_types = client.recv(header_size)

	header_json = header_types.decode(coding)

	header_dic = json.loads(header_json)

	total_size = header_dic['total_size']

	recv_size = 0
	recv_data = b''
	while recv_size < total_size:
		res = client.recv(1024)
		recv_data += res
		recv_size += len(res)
	print(recv_data.decode(coding))
client.close()

