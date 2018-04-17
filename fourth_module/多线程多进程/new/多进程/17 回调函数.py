# -*- coding: utf-8 -*-
"""
__title__ = '17 回调函数.py'
__author__ = 'yangyang'
__mtime__ = '2018.02.07'
"""
# 下载完所有页面以后，在去解析
# import requests
# from  multiprocessing import Pool
# import time,os
# def get_page(url):
# 	print('<%s> is getting [%s]' %(os.getpid(),url))
# 	response=requests.get(url)
# 	# time.sleep(2)
# 	print('<%s> is done [%s]' % (os.getpid(), url))
# 	return {'url':url,'text':response.text}
#
# def parse_page(res):
# 	print("<%s> parse [%s]"%(os.getpid(),res['url']))
# 	with open('content.txt','a') as f:
# 		parse_res = "[url]: %s [size]: %s\n"%(res['url'],len(res['text']))
# 		f.write(parse_res)
#
# if __name__ == '__main__':
# 	urls = [
# 		'https://www.baidu.com',
# 		'https://www.python.org',
# 		'https://www.openstack.org',
# 		'https://help.github.com/',
# 		'http://www.sina.com.cn/'
# 	]
# 	start = time.time()
# 	pool = Pool(4)
# 	obj_l = []
# 	for url in urls:
# 		obj = pool.apply_async(get_page,args=(url,))
# 		obj_l.append(obj)
# 	pool.close()
# 	pool.join()
# 	for obj in obj_l:
# 		parse_page(obj.get())
# 	# print([obj.get() for obj in obj_l])
# 	print("运行时间:%s"%(time.time()-start))  #3.499556064605713

# 回调函数  callback
import requests
from  multiprocessing import Pool
import time,os,random
def get_page(url):
	print('<%s> is getting [%s]' %(os.getpid(),url))
	response=requests.get(url)
	time.sleep(random.randint(1,7))
	# print('<%s> is done [%s]' % (os.getpid(), url))
	return {'url':url,'text':response.text}

def parse_page(res):
	print("<%s> parse [%s]"%(os.getpid(),res['url']))
	with open('content.txt','a') as f:
		parse_res = "[url]: %s [size]: %s\n"%(res['url'],len(res['text']))
		f.write(parse_res)

if __name__ == '__main__':
	urls = [
		'https://www.baidu.com',
		'https://www.python.org',
		'https://www.openstack.org',
		'https://help.github.com/',
		'http://www.sina.com.cn/'
	]
	start = time.time()
	pool = Pool(4)
	for url in urls:
		pool.apply_async(get_page,args=(url,),callback=parse_page)
	pool.close()
	pool.join()
	print("主进程PID：%s,运行时间:%s"%(os.getpid(),time.time()-start))



