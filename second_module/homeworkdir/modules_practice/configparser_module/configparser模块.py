#!/usr/bin/env python
#coding:utf-8


import configparser
conf = configparser.ConfigParser()        #生成一个conf对象
conf.read("conf.ini")
print(conf.sections())
print(conf.default_section)                #打印文件里面的组名（[] 括起来的名称）

print(list(conf["bitbucket.org"].keys()))    #打印当前组的key值，包括default的key值
print(conf["bitbucket.org"]['user'])         #打印key（'user'） 的值。

for k,v in conf['bitbucket.org'].items():      #循环打印 组['bitbucket.org'] 以及 [DEFAULT]组里面的值
    print(k,v)

if 'User' in conf['bitbucket.org']:         #判断某个值是否在组['bitbucket.org'] 和[DEFAULT] 里面。
    print('in')







