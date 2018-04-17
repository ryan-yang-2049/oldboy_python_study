#!/usr/bin/env python
#coding:utf-8

age = 19
def func01():
    global age   #==>等价于 把全局变量age=19 放到此处，然后此处的age还是全局变量
    def func02():
        print(age)
    age = 73      #==>此处的age还是全局变量，并且 age = 73
    func02()
func01()
print(age)
'''
从上面可以看出，在函数内部还是可以修改全局变量的。并且在函数内的局部变量的位置也是很有讲究的。
注重理解 global 以及局部变量的位置，就可以很好的利用嵌套函数了。但是逻辑稍微复杂，慎用
'''


