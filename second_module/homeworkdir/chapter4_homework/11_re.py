#!/usr/bin/env python
#coding:utf-8


# import  io,re
#
# f = io.open("re_test")
# pattern = re.compile("\w+\.(com|cn|edu)")
# for line in f.readlines():
#     res = re.search(pattern,line)
#     if res:
#         print(res.group())

#
#
# from  datetime import  datetime
# import  time
#
# now_time = int(time.time())
# print(now_time)
#
# expr_date = time.strptime("2021-01-01","%Y-%m-%d")
# print(int(time.mktime(expr_date)))


import hashlib

password = input("pwd:").strip()

hash_value = hashlib.md5()
hash_value.update(password.encode(encoding='utf-8'))
print(hash_value.hexdigest())



