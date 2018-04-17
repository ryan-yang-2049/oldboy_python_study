#coding:utf-8

import os
import sys

import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
print(BASE_DIR)

# from  atm.core import main
#
# if __name__ == '__main__':
#     main.run()
#
#
# '''
# python的包管理机制
# 代码注释，
# python 单元测试。单元库unittest
#
# 脚本只注重结果，开发关注过程，
# 开发：能给别人看懂，给自己看懂，交给机器处理。
#
# 递归（算法挂钩）。装饰器。
# '''



from core.main import run

if __name__ == '__main__':
    run()
