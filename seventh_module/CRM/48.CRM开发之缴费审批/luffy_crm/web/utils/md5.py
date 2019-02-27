# -*- coding: utf-8 -*-

# __title__ = 'md5.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.12.24'
import hashlib


def gen_md5(origin):
	"""
	md5 加密
	:param origin:
	:return:
	"""
	ha = hashlib.md5()
	ha.update(origin.encode('utf-8'))
	return ha.hexdigest()





