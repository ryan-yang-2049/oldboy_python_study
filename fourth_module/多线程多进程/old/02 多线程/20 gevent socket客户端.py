# -*- coding: utf-8 -*-
"""
__title__ = '20 gevent socket客户端.py'
__author__ = 'yangyang'
__mtime__ = '2018.02.05'
"""
from multiprocessing import Process
import socket
def client(server_ip,server_port):
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((server_ip,server_port))
    while True:
        client.send('hello'.encode('utf-8'))
        msg=client.recv(1024)
        print(msg.decode('utf-8'))

if __name__ == '__main__':
    for i in range(500):
        p=Process(target=client,args=('127.0.0.1',8088))
        p.start()











