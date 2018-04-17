#!/usr/bin/env python
#coding:utf-8

import configparser
import io

conf = configparser.ConfigParser()
conf.read("my.cnf")

conf.set("mysqld","default-time-zone","'+00:00'")

f = io.open("my.cnf",'w')
conf.write(f)
f.close()










