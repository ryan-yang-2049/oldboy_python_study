# -*- coding: utf-8 -*-

# __title__ = '08-插入排序.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.09.03'

# 时间复杂度 O(n**2)
def insert_sort(li):
	for i in range(1,len(li)): # i 表示摸到牌的下标
		temp = li[i]
		j = i - 1    # j指的是手里的牌的下标
		while j >=0 and li[j] > temp :  # 循环主要是找位置
			li[j+1] = li[j]
			j -= 1
		li[j+1] = temp
		print(li)


li = [5,2,3,7,6,9,8]
print(li)
insert_sort(li)
print(li)







