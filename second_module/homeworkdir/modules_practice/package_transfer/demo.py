# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'yangyang'
__mtime__ = '2018.01.02'
"""
import sys



# from package01.classOne import classOne
# from package02.classTwo import classTwo

# from package01 import *
# from package02 import *

import package01
import package02

if __name__ == "__main__":
    c1 = package01.classOne()
    c1.printInfo()
    c2 = package02.classTwo()
    c2.printInfo()

# 运行结果：
# Traceback (most recent call last):
#   File "D:/gitcode/...../package_transfer/demo.py", line 21, in <module>
#     c1 = package01.classOne()
# AttributeError: module 'package01' has no attribute 'classOne'