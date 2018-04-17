# -*- coding: utf-8 -*-
"""
__title__ = 'server_main.py'
__author__ = 'ryan'
__mtime__ = '2018/2/5'
"""
from socket import *
import time
server=socket(AF_INET,SOCK_STREAM)
server.bind(('127.0.0.1',8800))
server.listen(5)
server.setblocking(False)
print('starting...')
conn_l=[]
del_l=[]

while True:
    try:
        print(conn_l)
        conn,addr=server.accept()
        conn_l.append(conn)
    except BlockingIOError:         # 非阻塞I/O的情况下，无连接抛异常
        for conn in conn_l:
            try:
                data=conn.recv(1024)
                if not data:continue
                conn.send(data.upper())
            except BlockingIOError:
                pass
            except ConnectionResetError:  # 客户端断开连接抛异常
                del_l.append(conn)
        for obj in del_l:
            obj.close()
            conn_l.remove(obj)
        del_l=[]
