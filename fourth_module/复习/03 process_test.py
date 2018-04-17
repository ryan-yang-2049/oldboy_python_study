# -*- coding: utf-8 -*-
"""
__title__ = '03 process_test.py'
__author__ = 'yangyang'
__mtime__ = '2018.03.08'
"""

from multiprocessing import  Process

n=100

def work():
	global  n
	n=0
	print("子进程内：",n)

if __name__ == '__main__':
	p=Process(target=work)
	p.start()
	p.join()
	print("主进程内：",n)








