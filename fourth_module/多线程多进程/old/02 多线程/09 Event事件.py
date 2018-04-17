# -*- coding: utf-8 -*-
"""
__title__ = '09 Event事件.py'
__author__ = 'yangyang'
__mtime__ = '2018.02.01'
"""
#
# from threading import  Thread,Event
# import time
# event = Event()
# event2 = Event()
# # event.wait() 开始等待
# # event.set()  等待结束
#
# def student(name):
# 	print("学生 %s 正在听课"%name)
# 	event.wait()    #可以设置超时时间 event.wait(2)
# 	print("学生 %s 课间活动"%name)
# 	event2.wait()
# 	print("放学回家")
#
#
# def teacher(name):
# 	print("老师 %s 正在上课"%name)
# 	time.sleep(6)
# 	event.set()
#
# def go_home():
# 	event.wait()
# 	print("还有10分钟放学")
# 	time.sleep(10)
# 	event2.set()
#
# if __name__ == '__main__':
# 	stu1 = Thread(target=student,args=('alex',))
# 	stu2 = Thread(target=student,args=('wpq',))
# 	stu3 = Thread(target=student,args=('ryan',))
# 	t1 = Thread(target=teacher,args=('egon',))
# 	g1 = Thread(target=go_home)
#
# 	stu1.start()
# 	stu2.start()
# 	stu3.start()
# 	t1.start()
# 	g1.start()

#
#
# from  threading import Thread,Event,currentThread,Semaphore
# import time
# event = Event()
# sm = Semaphore(3)
#
# def conn():
# 	with sm:
# 		n=0
# 		while not event.is_set():
# 			if n == 3:
# 				print('%s try many times'%currentThread().getName())
# 				return
# 			n+=1
# 			print("%s try %s"%(currentThread().getName(),n))
# 			event.wait(0.5)
# 		print("%s in connected"%currentThread().getName())
#
#
# def check():
# 	print("%s is checking"%currentThread().getName())
# 	time.sleep(2)
# 	event.set()
#
# if __name__ == '__main__':
#
# 	t = Thread(target=check, name='check-connect-status')
# 	t.start()
# 	for i in range(2):
# 		t = Thread(target=conn, name='conn-%s' % i)
# 		t.start()



from threading import Thread,Event
import threading
import time,random
def conn_mysql():
    count=1
    while not event.is_set():
        if count > 3:
            # raise TimeoutError('链接超时')
            return
        print('<%s>第%s次尝试链接' % (threading.current_thread().getName(), count))
        event.wait(0.5)
        count+=1
    print('<%s>链接成功' %threading.current_thread().getName())


def check_mysql():
    print('\033[45m[%s]正在检查mysql\033[0m' % threading.current_thread().getName())
    # time.sleep(random.randint(2,4))
    time.sleep(1)
    event.set()
if __name__ == '__main__':
    event=Event()
    conn1=Thread(target=conn_mysql)
    conn2=Thread(target=conn_mysql)
    check=Thread(target=check_mysql)

    conn1.start()
    conn2.start()
    check.start()











