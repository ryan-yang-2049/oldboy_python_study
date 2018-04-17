# -*- coding: utf-8 -*-
"""
__title__ = '03 输入小写变大写-写到文件.py'
__author__ = 'ryan'
__mtime__ = '2018/2/7'
"""

from threading import Thread
import sys
msg_list = []
format_list = []

def talk():
	while True:
		msg = input(">>:").strip()
		if msg == 'exit':
			sys.exit()
		if not msg:continue
		msg_list.append(msg)


def format_msg():
	while True:
		if msg_list:
			res = msg_list.pop()
			format_list.append(res.upper())



def save():
	while True:
		if format_list:
			with open("db.txt",'a',encoding='utf-8') as f:
				res = format_list.pop()
				f.write('%s\n'%res)


if __name__ == '__main__':
	t1 = Thread(target=talk)
	t2 = Thread(target=format_msg)
	t3 = Thread(target=save)
	t1.start()
	t2.start()
	t3.start()
	print('主')




