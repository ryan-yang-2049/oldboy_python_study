#!/usr/bin/env python
#coding:utf-8


def send_alert(msg,*users):
    for u in users:
        print("报警发送给：%s "%u)

#如果参数中出现 *users，传递的参数就可以不再是固定个数，传过来的所有参数打包成元组
#方式一：
send_alert('cpu alert','a1','a2')
send_alert('cpu alert','u1','u2','u3')
#方式二：
#如果第二个参数不加 * 并且是列表，那么发送给 *users 的时候就会把列表当成是元组的第一个元素：（['u1','u2','u3'],）
#如果加了 * 那么就会变成（'u1','u2','u3'）
send_alert('cpu alert',*['u1','u2','u3'])


def send_alter02(msg,*args,**kwargs):
    print(msg,args,kwargs)
# **kwargs 接收的是字典参数。具体用法如下。
#方式一：

send_alter02('ryan',18,'SH',job='IT',num=1212) #结果：ryan (18, 'SH') {'job': 'IT', 'num': 1212}
#方式二：
dic = {'job':'IT','num':1212}
send_alter02('ryan','22',dic)  #结果：ryan ('22', {'job': 'IT', 'num': 1212}) {}
#结果就会出现*args 的第二种情况，因此应该使用下面这种方式：
send_alter02('ryan',25,**dic) #结果为：ryan (25,) {'job': 'IT', 'num': 1212}



