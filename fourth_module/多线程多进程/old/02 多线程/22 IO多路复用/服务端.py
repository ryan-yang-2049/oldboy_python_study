from socket import *
import time
import select
server=socket(AF_INET,SOCK_STREAM)
server.bind(('127.0.0.1',8809))
server.listen(5)
server.setblocking(False)
print('starting...')
reads_l=[server,]
while True:
    r_l,_,_=select.select(reads_l,[],[])
    print(r_l)
    for obj in r_l:
        if obj == server:
            conn,addr=obj.accept() #obj=server
            reads_l.append(conn)
        else:
            data=obj.recv(1024) #obj=conn
            obj.send(data.upper())
