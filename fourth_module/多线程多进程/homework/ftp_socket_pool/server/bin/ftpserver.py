# -*- coding: utf-8 -*-
"""
__title__ = 'ftpserver.py'
__author__ = 'yangyang'
__mtime__ = '2018.02.11'
"""
import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)
from server.core import server_main

if __name__ == '__main__':
	ip_port = ('127.0.0.1', 8905)
	myftp = server_main.FtpServer(ip_port)
	myftp.connect()

