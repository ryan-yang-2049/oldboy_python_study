# -*- coding: utf-8 -*-
"""
__title__ = 'ex01.py'
__author__ = 'yangyang'
__mtime__ = '2018.01.23'
"""

# sum_li = []
#
# for i in range(101):
# 	if i%3 != 0:
# 		sum_li.append(i)
#
# total_sum = sum(sum_li)
# print(total_sum)



__name = 'ryan'
__pass = '1234'
count = 0

while count <3:
	name = input("login：").strip()
	password = input("password:").strip()
	count += 1
	if name == __name and password == __pass:
		print("successful")
	else:
		print("login faild")







