# -*- coding: utf-8 -*-

# __title__ = '09-快速排序.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.09.03'
import time
import random
import copy
import sys
# 修改递归的最大深度
sys.setrecursionlimit(1000000)


# 计算函数运行时间的装饰器
def cal_time(func):
	def wrapper(*args,**kwargs):
		t1 = time.time()
		result = func(*args,**kwargs)
		t2 = time.time()
		print("%s running time: %s secs."%(func.__name__,t2-t1))
		return result
	return wrapper

@cal_time
def bubble_sort(li):
	for i in range(len(li)-1):  # 第i趟，从0开始
		exchange = False
		for j in range(len(li)-i-1): #列表内自循环，相当于列表里面的元素进行比较时的次数
			if li[j] > li[j+1]:         # 升序 > ,降序 <
				li[j],li[j+1] = li[j+1],li[j]   # 两个值进行交换
				exchange = True
		if not exchange:
			return

def partition(li,left,right):
	tmp = li[left]
	while left < right:
		while left<right and li[right] >= tmp: # 从右边找比tmp小的数
			right -= 1   # 往左移动一步
		li[left] = li[right]  # 把右边的值写到左边空位上
		while left < right and li[left] <= tmp:
			left += 1
		li[right] = li[left] # 把左边的值写到右边空位上
	li[left] = tmp  # 把tmp 归位
	return left

# 快速排序框架
def _quick_sort(data,left,right):
	if left < right:   # 至少2个元素
		mid = partition(data,left,right)
		_quick_sort(data,left,mid - 1)
		_quick_sort(data,mid + 1,right)

@cal_time
def quick_sort(li):
	_quick_sort(li,0,len(li)-1)


# li = [5,7,4,6,3,1,2,9,8]
# print(li)
# quick_sort(li)
# print(li)



li = list(range(10000))
random.shuffle(li)

li1 = copy.deepcopy(li)
li2 = copy.deepcopy(li)

quick_sort(li1)
bubble_sort(li2)

'''
结果：
quick_sort running time: 0.04754304885864258 secs.
bubble_sort running time: 14.84272313117981 secs.
'''