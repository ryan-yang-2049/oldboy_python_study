import socket

phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

phone.connect(('127.0.0.1',8084))

while True:
    msg=input('>>: ').strip()
    phone.send(msg.encode('utf-8'))
    data=phone.recv(1024)
    print(data.decode('utf-8'))

phone.close()