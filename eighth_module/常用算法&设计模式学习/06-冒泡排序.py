# -*- coding: utf-8 -*-

# __title__ = '06-冒泡排序.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.08.31'

# def bubble_sort(li):
# 	for i in range(len(li)-1):  # 第i趟，从0开始
# 		for j in range(len(li)-i-1): #列表内自循环，相当于列表里面的元素进行比较时的次数
# 			if li[j] > li[j+1]:         # 升序 > ,降序 <
# 				li[j],li[j+1] = li[j+1],li[j]   # 两个值进行交换
# 		print(li)
#
#
# li = [9,8,7,1,2,3,4,5,6]
# bubble_sort(li)
# 运行结果：
	# [8, 7, 1, 2, 3, 4, 5, 6, 9]
	# [7, 1, 2, 3, 4, 5, 6, 8, 9]
	# [1, 2, 3, 4, 5, 6, 7, 8, 9]
	# [1, 2, 3, 4, 5, 6, 7, 8, 9]
	# [1, 2, 3, 4, 5, 6, 7, 8, 9]
	# [1, 2, 3, 4, 5, 6, 7, 8, 9]
	# [1, 2, 3, 4, 5, 6, 7, 8, 9]
	# [1, 2, 3, 4, 5, 6, 7, 8, 9]

from cal_time import *

@cal_time
def bubble_sort(li):
	for i in range(len(li)-1):  # 第i趟，从0开始
		exchange = False
		for j in range(len(li)-i-1): #列表内自循环，相当于列表里面的元素进行比较时的次数
			if li[j] > li[j+1]:         # 升序 > ,降序 <
				li[j],li[j+1] = li[j+1],li[j]   # 两个值进行交换
				exchange = True
		# print(li)
		if not exchange:
			return

import random
# li = [9,8,7,1,2,3,4,5,6]
li = list(range(10000))
random.shuffle(li)
bubble_sort(li)




