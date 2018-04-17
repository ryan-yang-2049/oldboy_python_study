# -*- coding: utf-8 -*-
"""
__title__ = '客户端.py'
__author__ = 'ryan'
__mtime__ = '2018/2/5'
"""

from socket import *
client=socket(AF_INET,SOCK_STREAM)
client.connect(('127.0.0.1',8800))

while True:
    msg=input('>>: ').strip()
    if not msg:continue
    client.send(msg.encode('utf-8'))
    data=client.recv(1024)
    print(data.decode("utf-8"))


