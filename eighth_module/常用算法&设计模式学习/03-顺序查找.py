# -*- coding: utf-8 -*-

# __title__ = '03-顺序查找.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.08.31'

from cal_time import *

@cal_time
# li 表示列表；val表示待查找的元素
# 此时的时间复杂度为：O(n)
@cal_time
def linear_search(li,val):
	for ind,v in enumerate(li):
		if v == val:
			return ind
	else:
		return None



li = list(range(10000))



linear_search(li,3890)

