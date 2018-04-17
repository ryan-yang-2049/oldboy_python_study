# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'yangyang'
__mtime__ = '2018.01.17'
"""

# with open('a.txt','wb') as f:
# 	li = []
# 	for i in range(10001):
# 		if i != 100000:
# 			li.append(str(i)+',')
# 		else:
# 			li.append(str(i))
#
# 	value = (''.join(li)).encode('utf-8')
# 	f.write(value)
#
# with open('a.txt','rb') as read_file,open('b.txt','rb+') as read_write_file:
# 	content1 = read_file.read()
#
# 	print(len(content1))  # 101
#
#
# 	content2 = read_write_file.read()
# 	print("content2",len(content2))  #29

	# increase_content = content1[len(content2):]
	#
	# print("increase_content",len(increase_content))
	#
	# total_content = content2 + increase_content
	# print(total_content)
	# print("total_content",len(total_content))
	# if total_content == content1:
	# 	print("相同")
	# 	read_write_file.seek(len(content2))
	# 	read_write_file.write(increase_content)
	# 	read_write_file.truncate()

import os,hashlib






# def getfilemd5(filename):
# 	filemd5 = None
# 	if os.path.isfile(filename):
# 		f = open(filename,'rb')
# 		md5_obj = hashlib.md5()
# 		f.seek(0)
# 		pos = f.tell()
# 		data = f.read(8)
# 		content = ("%s%s"%(filename,data)).encode('utf-8')
# 		md5_obj.update(content)
# 		hash_code = md5_obj.hexdigest()
# 		f.close()
# 		filemd5 = str(hash_code).lower()
# 	return filemd5
# res = getfilemd5('b.txt')
# print(res)

#a.txt bfdf847d1b85ecd02be94cfdebe784e9
#a.txt 506da6771aebce3c2ba91ecb3694b1cb
#b.txt ddc5bc156444a85eaab340a69a457e69

#b.txt e4ef636f2fa5f1b8110f6ae908f0e9b8























