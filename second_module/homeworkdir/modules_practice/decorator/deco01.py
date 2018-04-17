# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'yangyang'
__mtime__ = '2018.01.02'
"""
import logging

#现在有一个新的需求，希望可以记录下函数的执行日志，于是在代码中添加日志代码
def use_logging(func):
    logging.warning("%s is running" % func.__name__)
    func()


def bar():
    print("i am bar")

use_logging(bar)

# 上面的代码，逻辑上不难理解，但是这样的话，我们每次都要将一个函数作为参数传递给use_logging 函数。
# 而且这种方式已经破坏了原有代码逻辑结构，之前执行业务逻辑时，执行运行 bar() ,但是现在不得不改成 use_logging(bar)。有没有更好的方式呢？答案是：装饰器。

