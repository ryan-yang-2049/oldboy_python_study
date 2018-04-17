#!/usr/bin/env python
#coding:utf-8

import os,sys,time
for i in range(101):
	hashes = '#' * int(i / 100.0 * 100)
	spaces = ' ' * (100 - len(hashes))
	sys.stdout.write("\r[%s] %d%%" % (hashes + spaces, i))
	sys.stdout.flush()
	time.sleep(0.05)