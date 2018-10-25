# -*- coding: utf-8 -*-

# __title__ = 'test.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.10.25'

import random

a='~!@#$%^&*()_+=?/|><.,'
special_string = "!@#$%&*_+="
num_string = "1234567890"
low_string = "abcdefghijklmnopqrstuvwxyz"
upper_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

total_string = []
for times in range(10):
	str_list = []
	for i in range(5):
		str_list.append(random.choice(low_string))
		str_list.append(random.choice(num_string))
		str_list.append(random.choice(special_string))
		str_list.append(random.choice(upper_string))

	password_string = "".join(str_list)
	last_string = password_string+"!dow"
	total_string.append(last_string)

print(total_string)

