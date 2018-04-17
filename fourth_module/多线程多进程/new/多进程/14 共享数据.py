# -*- coding: utf-8 -*-
"""
__title__ = '14 共享数据.py'
__author__ = 'yangyang'
__mtime__ = '2018.02.07'
"""

from multiprocessing import  Process,Manager,Lock
import time
def work(dic,mutex):
	# mutex.acquire()
	# dic['count'] -= 1
	# mutex.release()
	with mutex:
		dic['count'] -= 1
if __name__ == '__main__':
	mutex = Lock()
	m = Manager()
	share_dic = m.dict({'count':10})    # 所有进程可见
	p_l = []
	start = time.time()
	for i in range(10):
		p=Process(target=work,args=(share_dic,mutex,))
		p_l.append(p)
		p.start()
	for p in p_l:
		p.join()
	print(share_dic)
	print("运行时间：%s"%(time.time()-start))







