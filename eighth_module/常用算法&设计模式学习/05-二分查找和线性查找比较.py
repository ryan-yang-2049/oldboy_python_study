# -*- coding: utf-8 -*-

# __title__ = '04-二分查找.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.08.31'

import time

def cal_time(func):
	def wrapper(*args,**kwargs):
		t1 = time.time()
		result = func(*args,**kwargs)
		t2 = time.time()
		print("%s running time: %s secs."%(func.__name__,t2-t1))
		return result
	return wrapper

@cal_time
def linear_search(li,val):
	for ind,v in enumerate(li):
		if v == val:
			return ind
	else:
		return None

@cal_time
def binary_search(li,val):
	left = 0
	right = len(li) -1
	while left <= right:  #候选区还有值
		mid = (left + right) //2       #mid left right 都表示列表的小标索引
		if li[mid] == val:
			return mid
		elif li[mid] > val:  # 待查找的值在mid左侧
			right = mid-1
		else:  # li[mid] <val  待查找的值在mid右侧
			left = mid + 1

	else:    #没有找到，就是不符合  left 不小于等于 right
		return None


li = list(range(100000000))
linear_search(li,3338900)
binary_search(li,3338900)





