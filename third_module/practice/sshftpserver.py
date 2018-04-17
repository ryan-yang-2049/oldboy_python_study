'''
__title__ =  'ex04.py'
__author__ = 'ryan'
__mtime__ = '2018/1/17'
ssh ftp 服务端
'''
import os
import socket
import struct
import json
import subprocess

if os.name == 'posix':
	coding = 'utf-8'
elif os.name == 'nt':
	coding = 'gbk'

ip_port = ('127.0.0.1', 8099)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ip_port)
server.listen(5)

while True:
	conn, client_addr = server.accept()
	while True:
		try:
			cmd = conn.recv(8096)
			if not cmd: continue

			res = subprocess.Popen(cmd.decode(coding), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

			stdout = res.stdout.read()
			stderr = res.stderr.read()

			res_dic = {'total_size': len(stdout) + len(stderr)}

			res_json = json.dumps(res_dic)

			res_bytes = res_json.encode(coding)

			conn.send(struct.pack('i', len(res_bytes)))

			conn.send(res_bytes)

			conn.send(stdout)
			conn.send(stderr)

		except ConnectionResetError:
			break
	conn.close()
server.close()