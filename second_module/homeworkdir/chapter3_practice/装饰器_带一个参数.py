#!/usr/bin/env python
#coding:utf-8

def auth(func):
    def user_auth(arg):
        print('--before--')
        func(arg)
        print('--after--')
    return user_auth

@auth
def one(arg):
    print('I',arg)

if __name__ == '__main__':
    one("love you")
'''
[root@js-93 wrap]# python3 exam03.py
--before--
I love you
--after--
运行过程 查看例1，这个主要注意的是，当被装饰的函数带一个参数的时候，装饰器应该怎么写。
'''