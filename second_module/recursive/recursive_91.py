# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'yangyang'
__mtime__ = '2017.12.28'
"""

'''
n! = 1 * 2 * 3 * 4 * 5*……*n
n! = (n-1)! * n
'''
#n! = 1 * 2 * 3 * 4 * 5*……*n
# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n-1)
#
# print(fact(4))

# def fact(n):
#     print("factorial has been called with n = " + str(n))
#     if n == 1:
#         res = 1
#         return res
#     else:
#         res = n * fact(n - 1)
#         print("intermediate result for ", n, " * fact(", n - 1, "): ", res)
#         return res
#
#
# print(fact(5))
#


# def dict2flatlist(d, l):
#     print(d)
#     for x in d.keys():
#         if type(d[x]) == dict:
#             dict2flatlist(d[x], l)
#         else:
#             l.append(d[x])
#
#
# d = {1: "a", 2: "b", 3: {4: "c", 5: "d", 6: {7: "e"}}, 8: "f"}
#
# l = []
# dict2flatlist(d, l)
# print(l)


# dic = {'ryan1':{'B1':'python'},'cherry1': {'S1':'go'},'ryan2':{'B1':'python'},'cherry2': {'S1':'go'}}
#
# li = []
#
# def dict2flatlist(d, l):
#     # print(d)
#     for x in d.keys():
#         if x != 'B1':
#             if type(d[x]) == dict:
#                 print("1x",x)
#                 # if d[x].value
#                 dict2flatlist(d[x], l)
#                 # print("1==>",d[x])
#         else:
#             l.append(d.keys())
#
#
# dict2flatlist(dic,li)
# print(li)


def recursive(dic, li, arg):
    for key in dic.keys():
        if type(dic[key]) == dict:
            for k, v in dic[key].items():
                if k == arg:
                    li.append(key)
                else:
                    recursive(dic[key],li,arg)

dic = {'ryan1':{'B1':'python'},'cherry1': {'S1':'go'},'ryan2':{'B1':'python'},'cherry2': {'S1':'go'},'ryan3':{'ryan4':{'B1':'python'}}}

li = []
arg = 'B1'
recursive(dic,li,arg)
print(li)

















