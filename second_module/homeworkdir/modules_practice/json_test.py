#!/usr/bin/env python
#coding:utf-8

import json
data = {
    'roles':[
        {'role':'monster','life':50},
        {'role':'hero','life':80},
    ]
}

'''dump 转成字符串，然后直接把数据写到磁盘（文件）'''
f = open("test.json",'w')
json.dump(data,f)
f.close()


'''dumps 仅转成字符串，然后通过文件的写方法，写到文件'''
f = open("test.json",'w')
d = json.dumps(data)
f.write(d)
f.close()


'''load 直接读取磁盘内容'''
f = open("test.json",'r')
data = json.load(f)
f.close()

'''loads 先读取到内存，在从内存读取出来'''
f = open("test.json",'r')
d = f.read()
data = json.loads(d)
f.close()


