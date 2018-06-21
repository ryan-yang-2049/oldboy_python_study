# -*- coding: utf-8 -*-

# __title__ = 'urlconverter.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.06.21'

class MonConvert(object):

	regex = "[1-9]{1}|1[0-2]{1}"

	def to_python(self,value):
		return int(value)

	def to_url(self,value):    #反向解析
		return '%04d'%value









