# -*- coding: utf-8 -*-
"""
__title__ = '19 gevent socket服务端.py'
__author__ = 'yangyang'
__mtime__ = '2018.02.05'
"""


from gevent import monkey;monkey.patch_all()
import gevent
import socket
def talk(conn,addr):
    while True:
        data=conn.recv(1024)
        print('%s:%s %s' %(addr[0],addr[1],data))
        conn.send(data.upper())
    conn.close()

def server(ip,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((ip,port))
    s.listen(5)
    while True:
        conn,addr=s.accept()
        gevent.spawn(talk,conn,addr)
    s.close()

if __name__ == '__main__':
    server('127.0.0.1', 8088)




