import socket

#1、买手机
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# phone= <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('0.0.0.0', 0)>

#2、绑定手机卡
phone.bind(('127.0.0.1',8080)) #0-65535:0-1024给操作系统使用

#3、开机
phone.listen(5)             #listen 表示最大挂起的连接数

#4、等电话链接
print('starting...')
conn,client_addr = phone.accept()
# conn: <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8080), raddr=('127.0.0.1', 63377)>
# client_addr: ('127.0.0.1', 63377)

#5、收，发消息
data=conn.recv(1024) #1、单位：bytes 2、1024代表最大接收1024个bytes
print('客户端的数据:',data)
conn.send("服务端返回：".encode("utf-8")+data.upper())  #发送给客户端

#6、挂电话
conn.close()

#7、关机
phone.close()