# -*- coding: utf-8 -*-
"""
__title__ = '13 线程queue.py'
__author__ = 'yangyang'
__mtime__ = '2018.02.08'
"""


# 先进先出-->队列
import queue
q=queue.Queue(3)
# 队列存数据，因为上面设置的队列的大小是3，因此，只能存放3次数据,如果存的数据超过了设置的大小，则程序会卡在原地
q.put('first')
q.put(2)
q.put('third')
q.put_nowait(4)
'''
放入数据的次数超过了存设置的大小会抛出异常。
q.put(4)
q.put(4,block=False) # 默认block的值是True，如果不设置为False,那么程序就会卡在这里如果设置为False以后，运行程序会抛出异常 "queue.Full"
q.put(4,block=True,timeout=3)  # 如果 timeout=3 3秒以内没有去做，也抛出异常 "queue.Full"，此时里面的block=True没有意义，因为,默认为True
q.put_nowait(4)  # 也抛出异常 "queue.Full"，相当于  q.put(4,block=False)
'''

# 队列取数据，取的时候也一样，如果取得值超过了队列存的值，程序也会卡在原地
# print("取数据1",q.get())
# print("取数据2",q.get())
# print("取数据3",q.get())
'''
取数据的次数超过了放数据的次数，也会抛出异常，结论和put差不多。
print("取数据4",q.get(block=False,timeout=3))  # 和存数据一样的理解：抛出异常 "queue.Empty"
print(q.get_nowait())       # 当队列里面为空时，抛出异常 "queue.Empty"
'''


# '''
# 堆栈
# import queue
# q = queue.LifoQueue(3)   # 后进先出   --> 堆栈
# q.put('first')
# q.put(2)
# q.put('third')
#
# print("取数据1",q.get())
# print("取数据2",q.get())
# print("取数据3",q.get())
#
#
# 结果：
# 	取数据1 third
# 	取数据2 2
# 	取数据3 first
# '''
# import queue
# q = queue.PriorityQueue(3)  # 优先级队列
# q.put((10,'one'))          # q.put((优先级，数据))  数字越小，优先级越高
# q.put((40,'two'))
# q.put((30,'three'))
#
# print("取数据1",q.get())
# print("取数据2",q.get())
# print("取数据3",q.get())









