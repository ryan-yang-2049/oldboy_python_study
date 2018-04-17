#!/usr/bin/env python
#coding:utf-8

# def calc(n):
#     n = int(n/2)
#     print(n)
#     if n > 0:
#         calc(n)
#     return n
# print(calc(10))

'''
执行顺序： calc(10)-->calc(5)-->calc(2)-->calc(1)-->calc(0)-->calc(0)-->calc(1)-->calc(2)-->calc(5)-->calc(10)退出
"calc(0)-->calc(1)-->calc(2)-->calc(5)" 这里的意思是（结合函数的后面两句代码），当n=0时，打印print（0）。但是递归的时候的函数执行
相当于是一层函数包含着一层函数，因此，退出的时候就会去执行获得 n=0 时 calc(n)里面n的值，此时n=1，这里在补充一点，此时的函数不在是往下递归，
而是去退出整个函数，但是，在退出一层函数，也就是当 n=1 时，calc(n) 里面n的值是多少，再去打印n值。以此类推。
'''


#递归返回值
def calc(n,count):
    print(n,count)
    if count < 5:
        return calc(n/2,count+1)
    else:
        return n

res = calc(100,1)
print(res)
'''
递归的返回值：两个return 缺一不可。因为，如果只有一个else 的return，在返回的时候就会退到上一层，但是上一层没有返回值。因此，就会得到一个None的值。
如果没有else的return，那么当count=5 以后就开始退出函数了，也就更没有返回值了。这里可以根据上面（特指递归的执行顺序的例子）的的递归顺序去理解，
之所以会退出，是因为上面的n=0，然后一直往回退。因此，在count=5时返回给上一层以后，count=4 但是 此时没有返回值，所以更不行！
'''


























