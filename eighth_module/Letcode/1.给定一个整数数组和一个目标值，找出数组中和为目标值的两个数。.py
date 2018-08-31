# -*- coding: utf-8 -*-

# __title__ = '1.给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.08.31'
#
# 给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
#
# 你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。
#
# 示例:
#
# 给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]

# a = target - b
import time

def cal_time(func):
	def wrapper(*args,**kwargs):
		t1 = time.time()
		result = func(*args,**kwargs)
		t2 = time.time()
		print("%s running time: %s secs."%(func.__name__,t2-t1))
		return result
	return wrapper

class Solution(object):
	@cal_time
	def twoSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		for i in range(len(nums)):
			for j in range(i+1,len(nums)):
				if nums[i] + nums[j] == target:
					return [i,j]

nums = [2, 3,7, 11,3, 15]
target = 6
s = Solution()
print(s.twoSum(nums, target))