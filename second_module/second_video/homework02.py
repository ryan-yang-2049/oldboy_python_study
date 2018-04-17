#coding:utf-8
'''
1. 用python函数实现一个斐波那契数列
2. 写一个装饰器
  a. 编写3个函数，每个函数执行的时间是不一样的， 提示：可以使用time.sleep(2)，让程序sleep 2s或更多，
  b. 编写装饰器，为每个函数加上统计运行时间的功能 提示：在函数开始执行时加上start=time.time()就可纪录当前执行的时间戳，函数执行结束后在time.time() - start就可以拿到执行所用时间
  c. 编写装饰器，为函数加上认证的功能，即要求认证成功后才能执行函数
  d. 编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件），要求登录成功一次，后续的函数都无需再输入用户名和密码

'''

# q1.
# def  fib(max):
#     n,a,b = 0,0,1
#     while n < max:
#         print(b)
#         a,b = b,a+b
#         n += 1
# fib(20)
#q2
#
# import time
#
# def remeber_time(time_set):
#     def outer(func):
#         def wrapper(*args,**kwargs):
#             wrap_time = time.time()
#             time.sleep(time_set)
#             return func(wrap_time,*args,**kwargs)
#         return wrapper
#     return outer
#
# @remeber_time(time_set=3)
# def func01(wrap_time):
#     for i in range(10):
#         i += 1
#     run_time = time.time() - wrap_time
#     print("01 local time",run_time)
#
# @remeber_time(time_set=5)
# def func02(wrap_time):
#     for i in range(15):
#         i += 1
#     run_time = time.time() - wrap_time
#     print("02 local time",run_time)
#
#
# @remeber_time(time_set=4)
# def func03(wrap_time):
#     for i in range(8):
#         i += 1
#     run_time = time.time() - wrap_time
#     print("03 local time",run_time)
#
#
# func01()
#
# func02()
#
# func03()


# login_status = False
# def login_auth(func):
#     def inner(*args,**kwargs):
#
#         global login_status
#         if login_status == False:
#             _name = 'ryan'
#             _password = '1234'
#             login_name = input("login:").strip()
#             login_password = input("password:").strip()
#             if login_password == _password and login_name == _name:
#
#                 login_status = True
#                 # func(*args,**kwargs)
#             else:
#                 print("权限不足!")
#         else:
#             func(*args,**kwargs)
#     return inner
#
#
#
#
# @login_auth
# def run():
#     print("1+1=",1+1)
#
# @login_auth
# def run02():
#     print("2+2=",2+2)


