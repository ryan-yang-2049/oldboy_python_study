# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'yangyang'
__mtime__ = '2018.01.04'
"""


import io

def read_file(file_name):
    BLOCK_SIZE = 10
    with io.open(file_name,'r',encoding='utf-8') as read_f:
        while True:
            block = read_f.read(BLOCK_SIZE)
            if block:
               yield block
            else:
                return


line = read_file('log.txt')

for i in line:
    print(i)

