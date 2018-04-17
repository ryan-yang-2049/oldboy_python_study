# -*- coding: utf-8 -*-
"""
__title__ = '06 serverjd.py'
__author__ = 'yangyang'
__mtime__ = '2018.02.27'
"""


import socket

sock=socket.socket()

sock.bind(("127.0.0.1",8800))

sock.listen(5)

while 1:
    print("waiting........")
    conn,addr=sock.accept()

    data=conn.recv(1024)
    print("data",data.decode("utf8"))

    with open("index.html","r") as f:

        response=f.read()

    conn.send(("HTTP/1.1 201 OK\r\n\r\n%s"%response).encode("utf8"))







