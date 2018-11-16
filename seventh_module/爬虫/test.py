# -*- coding: utf-8 -*-

# __title__ = 'test.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.11.16'



pageNum = 1
url = 'https://www.qiushibaike.com/text/page/%d/'
if pageNum <= 13:
	pageNum += 1
	new_url = format(url%pageNum)
	print(new_url)







