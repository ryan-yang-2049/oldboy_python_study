#!/usr/bin/env python
#coding:utf-8

import configparser
conf = configparser.ConfigParser()        #生成一个conf对象
conf.read("conf_test.ini")

print(dir(conf))

#读取
print(conf.options('group1'))    #读到组 group1 里面的key  result:['k1', 'k2']
print(conf['group1']['k2'])      #获取对应key的value    reslut: v2

item_list = conf.items('group1')
print(item_list)                  #result: [('k1', 'v1'), ('k2', 'v2')]

#增加
#方法一：
conf.add_section("group3")
conf["group3"]['name'] = 'ryan'
conf["group3"]['age'] = '18'
# 方法二：
conf.add_section("group4")
conf.set("group4",'address','SH')
conf.set("group4",'PHONE','1234')
f = open("conf_test_new.ini",'w')
conf.write(f)
f.close()

#删除
conf02 = configparser.ConfigParser()        #生成一个conf对象
conf02.read("conf_test_new.ini")
#删除一个key值
conf02.remove_option("group4","address")
f = open("conf_test_new.ini",'w')
conf02.write(f)
f.close()
#删除一个section
conf02.remove_section("group4")
f = open("conf_test_new.ini",'w')
conf02.write(f)
f.close()



