
'''
在类内部定义的函数，分为两大类：
    一：绑定方法:绑定给谁，就应该由谁来调用，谁来调用就回把调用者当作第一个参数自动传入
        绑定到对象的方法：在类内定义的没有被任何装饰器修饰的

        绑定到类的方法：在类内定义的被装饰器classmethod修饰的方法

    二：非绑定方法:没有自动传值这么一说了，就类中定义的一个普通工具，对象和类都可以使用
        非绑定方法：不与类或者对象绑定



'''

class Foo:
    def __init__(self,name):
        self.name=name

    def tell(self):                 #绑定给对象
        print('名字是%s' %self.name)

    @classmethod                    #绑定给类
    def func(cls): #cls=Foo
        print(cls)

    @staticmethod                   #非绑定方法，类和对象都可以使用（普通函数）
    def func1(x,y):
        print("x + y =",x+y)

f=Foo('egon')

print("类的普通函数：",Foo.tell)        # 类的一个普通函数    调用：Foo.tell(f)
print("绑定到对象的方法：",f.tell)       # 绑定到对象的方法  调用：f.tell()

print("绑定到类的方法：",Foo.func)       # 绑定到类的方法  Foo.func() #等价于 print(Foo)

print("非绑定方法,给类使用:",Foo.func1)  # 非绑定方法，给类使用
print("非绑定方法,给使用:",f.func1)      # 非绑定方法，给对象使用

Foo.func1(1,2)                  #非绑定方法，该怎么传参就怎么传参
f.func1(1,3)                    #非绑定方法，该怎么传参就怎么传参