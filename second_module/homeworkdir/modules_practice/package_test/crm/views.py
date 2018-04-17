#!/usr/bin/env python
#coding:utf-8
import sys,os
#
# # print(__file__)
# #"__file__"表示的是当前py文件的绝对路径位置，包含当前py文件名称
#
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from proj import settings

# from crm import  models
# def sayhi():
#     print("hello world")
#
# models.model()