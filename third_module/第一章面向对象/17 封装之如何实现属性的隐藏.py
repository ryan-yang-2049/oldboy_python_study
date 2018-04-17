# class A:
#     __x=1 #_A__x=1
#     def __init__(self,name):
#         self.__name=name #self._A__name=name
#
#     def __foo(self): #def _A__foo(self):
#         print('run foo')
#
#     def bar(self):
#         self.__foo() #self._A__foo()
#         print('from bar')

# print(A.__dict__)
# print(A.__x)
# print(A.__foo)

# a=A('egon')
# a._A__foo()
# a._A__x

# print(a.__name) #a.__dict__['__name']
# print(a.__dict__)
#
# a.bar()

'''
封装不是单纯意义上的隐藏。
变量名或者方法名前面加上双下划线（“__”）就可以实现隐藏。就类定义阶段就会发生变形。
这种变形的特点：
    1、在类外部无法直接obj.__AttrName
    2、在类内部是可以直接使用：obj.__AttrName (在定义阶段已经正确访问了)
    3、子类无法覆盖父类__开头的属性
'''

# class Foo:
#     def __func(self): #_Foo__func
#         print('from foo')
#
#
# class Bar(Foo):
#     def __func(self): #_Bar__func
#         print('from bar')

# b=Bar()
# b.func()



# class B:
#     __x=1
#
#     def __init__(self,name):
#         self.__name=name #self._B__name=name


#验证问题一：
# print(B._B__x)

#验证问题二：
# B.__y=2
# print(B.__dict__)
# b=B('egon')
# print(b.__dict__)
#
# b.__age=18
# print(b.__dict__)
# print(b.__age)


#验证问题三：
class A:
    def __foo(self):    # _A__foo()
        print('A.foo')

    def bar(self):
        print('A.bar')
        self.__foo() #self._A__foo()

class B(A):
    def __foo(self): #_B__foo()
        print('B.foo')

b=B()
b.bar()



# class A:
#     __x=1   #在类被定义的时候已经变形为：_A__x
#     def __init__(self,name):
#         self.__name = name  #变形为：_A__name
#
#     def __foo(self): #变形为： _A__foo
#         print('A.foo')
#
#     def tell_info(self):
#         print("隐藏的属性x:",self.__x)
#         print("隐藏的属性name:",self.__name)
#
#     def bar(self):
#         print('A.bar')
#         self.__foo() #变形为： self._A__foo()
#
# class B(A):
#     def __foo(self): #变形为： _B__foo
#         print('B.foo')



# obj=A('ryan')
'''错误调用隐藏的方法'''
# print(obj.__x)  #AttributeError: 'A' object has no attribute '__x'
'''正确的调用隐藏的方法，但是在python中，如果在类里面已经设置好了隐藏属性，那在外部就尽量
不要改变，如果要求调用或者改变它，那就直接不要“__”就可以了'''
# print(obj._A__x)
#
# print(obj.__dict__)

# obj=A('ryan')
# obj.tell_info()
#
# obj=A('ryan')
# print(obj.__dict__)
# obj.__age = 18
# print(obj.__dict__)


