# -*- coding: utf-8 -*-

# __title__ = 'app.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.12.13'


import utils

print(utils.site)   # <utils.AdminSite object at 0x0000021C493481D0>


# import utils
# print(utils.site)   # <utils.AdminSite object at 0x0000021C493481D0>

import commons

"""
在python中，如果已经导入过的文件再次被重新导入时，python不会重新在解释一遍，而是选择从内存中直接将原来导入的值拿来用
"""




