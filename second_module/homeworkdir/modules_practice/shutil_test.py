#!/usr/bin/env python
#coding:utf-8

import  shutil

f1 = open("test.txt",'r')
f2 = open("test_new.txt",'w')

shutil.copyfileobj(f1,f2,length=3)




