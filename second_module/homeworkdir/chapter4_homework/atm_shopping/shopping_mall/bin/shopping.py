# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'yangyang'
__mtime__ = '2017.12.25'
"""


import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)
from atm.core.file_operate import operate_user_info_file

from atm.core.user_auth import login_auth


from  shopping_mall.shop_core import main

if __name__ == '__main__':
    run()



