#coding:utf-8
#-*- encoding=utf-8 -*-
from functools import wraps

def task_logging():
    def func_wrapper(func):
        @wraps(func)
        def return_wrapper(*args, **wkargs):
            # 函数通过装饰起参数给装饰器传送参数
            taskname = input("name:")
            print('before task',taskname)
            # 装饰器传变量给函数
            taskid = 1
            summer, funcres = func(taskid, *args, **wkargs)
            print('after task', taskid, summer)
            return funcres
        return return_wrapper
    return func_wrapper

@task_logging()
def abcd(taskid):
    print("testd runing",taskid)
    return "task summer success eg", []

print(abcd())

'''
name:alex
before task alex
testd runing 1
after task 1 task summer success eg
[]
'''