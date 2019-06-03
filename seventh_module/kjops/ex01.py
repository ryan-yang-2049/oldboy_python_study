# -*- coding: utf-8 -*-

# __title__ = 'ex01.py'
# __author__ = 'Administrator'
# __mtime__ = '2019/6/2'

str = "笔记本"

ASSET_TYPE_CHOICE = (
		(1, "笔记本"),
		(2, "台式机"),
		(3, "显示器"),
	)

for i in ASSET_TYPE_CHOICE:
	print(i[1])
	if i[1] == str:
		print(i[0])
		break









