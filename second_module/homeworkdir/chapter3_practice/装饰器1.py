#!/usr/bin/env python3
#coding:utf-8
def auth(func):
    def user_auth():
        print('before')
        func()
    return user_auth

def one():
    print('one')

temp = auth(one)
one = temp

def two():
    print('two')
two = auth(two)

@auth
def three():
    print('three')

if __name__ == '__main__':
    print('-----one method-----')
    one()
    print('-----two method-----')
    two()
    print('-----three method-----')
    three()

'''
[root@js-93 wrap]# python3 exam02.py
-----one method-----
before
one
-----two method-----
before
two
-----three method-----
before
three

代码理解：可以看出三种方式都相当于装饰器的效果，明显的可以看出第三种方法（@auth），简单明了，而且已用性很高。
整体代码解释：
当执行整个脚本的时候，是从上到下依次执行的，当执行到函数的时候，这个时候并没有在程序中调用该函数，因此，解释器会把该函数名称先读取到内存中，而不去读取函数里面代码的过程。依次往下读直到13,14行。
第一种方法：
当读到13行和14 行的时候，“temp = auth(one)”，这个时候已经调用了函数“auth”,并且传递参数“one”，因此，解释器会去执行该函数。执行auth函数的时候，先执行"return user_auth"(前面提到过，只有函数被被调用的时候才能执行函数，后面不在提及)，
然后执行“user_auth”函数，会打印“before”，然后在调用“fun()”函数。函数“func”在去执行“print('one')”，就得带了后面 “one method”的结果。这里要注意的是，在函数“one（）”函数下面的 temp = auth(one) 以及 one = temp的含义；
下面两句的含义:
temp = auth(one) 
one = temp
这两句的含义，其实等价于 方法2 的 two = auth(two)，也就是 one = auth(one) 此时的one不在执行 print('one')了，因为，one已经被重新定义了，他会去执行auth(one)。
第二种方法：
第二种方法和第一种方法理解基本一样。
第三种方法：（理解于：http://www.cnblogs.com/wupeiqi/articles/4980620.html）
当写完代码以后，函数未被执行，Python解释器就会从上到下解释代码，步骤如下：
1. def  auth(func):    --->将auth函数加载到内存。
2. @auth  
如果把代码分离，只剩下第三种方法，那么，从代码表面看，解释器仅仅会执行上面2个过程，因为，函数没有被调用之前，其内部代码不会被执行。
从表面上看解释器确实会执行这两句，但是 @auth 这一句代码里面却有大文章，@函数名 是python的一种语法糖。
从上例@auth内部会执行一下操作：
执行auth函数，并将 @auth下面的函数作为auth函数的参数，即：@auth 等价于 auth（three）
所以，内部会去执行：
 def auth(three):
      def user_auth():
         print('before')
         three()
     return user_auth
将执行完的auth函数返回值 赋值给 @auth 下面的 函数的函数名。
auth函数的返回值是，print brfore 以及 执行，three()
这就是装饰器的进化过程。
'''