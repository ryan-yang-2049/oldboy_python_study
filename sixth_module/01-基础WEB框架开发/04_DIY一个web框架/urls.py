# -*- coding: utf-8 -*-

# __title__ = 'urls.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.06.19'

from  views import *
url_patterns = [
	("/login", login),
	("/index", index),
	("/favicon.ico",fav),
	("/timer",timer),
	("/auth",auth),
]





