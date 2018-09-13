# -*- coding: utf-8 -*-

# __title__ = '07-选择排序.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.08.31'

# 简单版，不推荐
def select_sort_simple(li):
	li_new = []
	for i in range(len(li)):   # 时间复杂度 O(n)
		min_val = min(li)      # 时间复杂度 O(n)
		li_new.append(min_val)
		li.remove(min_val)     # 时间复杂度 O(n)
	return li_new

# 进阶版
def select_sort(li):
	for i in range(len(li)-1):   # i 是第几趟
		min_loc = i   #记录最小值的位置，用于交换
		for j in range(i+1,len(li)):
			if li[j] < li[min_loc]:
				min_loc = j
		li[i],li[min_loc] = li[min_loc],li[i]
		print(li)


li = [3,5,7,8,4,2,1]
print(li)
# print(select_sort_simple(li))
select_sort(li)






