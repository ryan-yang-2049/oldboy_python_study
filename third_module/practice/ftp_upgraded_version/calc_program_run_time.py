# -*- coding: utf-8 -*-
"""
__title__ = 'calc_program_run_time.py'
__author__ = 'yangyang'
__mtime__ = '2018.01.30'
"""
import time
from datetime import  datetime




def date_time_str(date_time):
	date_time_format = '%y-%M-%d %H:%M:%S'
	return datetime.strftime(date_time,date_time_format)

def timer(func):
	def decor(*args):
		print("程序运行时间：",date_time_str(datetime.now()))
		time.sleep(2)
		func(*args)
		print("程序结束时间：",date_time_str(datetime.now()))
	return decor

@timer
def printSth(str, count):
	for i in range(count):
		pass
		# print("%d hello,%s!"%(i,str))



printSth("world", 1000000)











