import socket

phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.bind(('127.0.0.1',8084)) #0-65535:0-1024给操作系统使用
phone.listen(5)

print('starting...')
conn,client_addr=phone.accept()
print(client_addr)

while True: #通信循环
    data=conn.recv(1024)
    print('客户端的数据',data.decode('utf-8'))

    conn.send("服务端返回：".encode('utf-8')+data)

conn.close()
phone.close()


