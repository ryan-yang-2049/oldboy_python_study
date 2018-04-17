#coding:utf-8

import  socket,struct,json


ip_port = ('127.0.0.1',8080)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ip_port)


while True:
	cmd = input(">>:").strip()
	if not cmd:continue
	client.send(cmd.encode('utf-8'))

	recv_res = client.recv(4)

	header_size = struct.unpack('i',recv_res)[0]

	header_types = client.recv(header_size)

	header_json = header_types.decode('utf-8')

	header_dict = json.loads(header_json)

	total_size = header_dict['total_size']

	recv_szie = 0
	recv_data = b''

	while recv_szie < total_size:
		res = client.recv(1024)
		recv_data += res
		recv_szie += len(res)

	print(recv_data.decode('utf-8'))

client.close()








