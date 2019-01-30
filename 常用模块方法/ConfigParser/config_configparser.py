# -*- coding: utf-8 -*-

# __title__ = 'config_configparser.py'
# __author__ = 'YangYang'
# __mtime__ = '2019.01.29'

import configparser
import re
import os
'''
"[ ]"包含的为 section，section 下面为类似于 key - value 的配置内容； 
configparser 默认支持 '=' ':' 两种分隔。

'''
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
conf_file = os.path.join(BASE_DIR,'cmdb.conf')
conf = configparser.ConfigParser()
conf.read(conf_file)

# 1.获取配置文件里面 数据的信息
# if conf.get('db','engine') == 'mysql':
# 	DB_HOST = conf.get('db', 'host')
# 	DB_PORT = conf.getint('db', 'port')
# 	DB_USER = conf.get('db', 'user')
# 	DB_PASSWORD = conf.get('db', 'password')
# 	DB_DATABASE = conf.get('db', 'database')

# 默认section
# print(conf.default_section)

# 所有的section
# print(conf.sections())


# 找到 db下所有的配置，包含DEFAULT
# print(list(conf["db"].keys()))
# print(conf.options('db'))

# 找到 db下 port 的值
# print(conf["db"]['port'])

# 循环db 下所有的key和value
# for k,v in conf['db'].items():
# 	print(k,v)


# 读取配置文件的方法 注意：都包含了DEFAULT的配置
# print(conf.options('db'))   # ['engine', 'host', 'port', 'user', 'password'...]
# print(conf.items('db')) # [('user', 'root'), ('password', '123456'), ('database', 'adminset')......]

# 增加  直接写入到配置文件里面
# conf.add_section('mongodb')
# conf.set('mongodb','mongodb_ip','127.0.0.1')
# conf.set('mongodb','mongodb_port','27017')
# conf.set('mongodb','mongodb_user','root')
# conf.set('mongodb','mongodb_pwd','1234')
# conf.set('mongodb','collection','sys_info')
# f = open(conf_file,'w')
# conf.write(f)
# f.close()


# 删除一个section下面的key
# conf.remove_option('topsecret.com','port')
# f = open(conf_file,'w')
# conf.write(f)
# f.close()

# 删除一个section
# conf.remove_section('topsecret.com')
# f = open(conf_file,'w')
# conf.write(f)
# f.close()




























