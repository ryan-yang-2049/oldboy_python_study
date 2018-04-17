#!/usr/bin/env python
#coding:utf-8
f_name = "text.log"
old_str = "python"
new_str = "java"
f = open(f_name,'r+',encoding="utf-8")
list01 = []
for line in f:
	if old_str in line:
		line = line.replace(old_str,new_str)
	list01.append(line)
values = ''.join(list01)
print(values)
f.seek(0)
f.write(values)
f.truncate()
f.close()












