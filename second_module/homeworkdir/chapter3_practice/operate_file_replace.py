#!/usr/bin/env python
#coding:utf-8

'''
写一个脚本，运行用户按以下方式执行，即可以对指定文件内容进行全局替换
python your_script.py old_str new_str filename
替换完毕以后打印替换了多少处内容
'''
'''
文本例子
[root@dev second_modules]# cat text.log
hello world!
everyday study python
l like python
do you love python?
'''
import sys
def replace_str(filename,old_str,new_str):
	content_list = []
	replace_times = 0
	f = open(filename,'r+')
	for line in f:
		if old_str in line:
			line = line.replace(old_str,new_str)
			replace_times += 1
		content_list.append(line)
	values = ''.join(content_list)
	f.seek(0)
	f.write(values)
	f.truncate()
	return replace_times

if '__main__' == __name__:
	old_str = sys.argv[1]
	new_str = sys.argv[2]
	filename = sys.argv[3]
	times = replace_str(filename,old_str,new_str)
	print("replace total numbers:%d"%times)
'''
执行结果：
[root@dev second_modules]# python operate_file_replace.py  python java text.log
replace total numbers:3
'''











