# -*- coding: utf-8 -*-

# __title__ = '7.class_iter的用法.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.12.21'




class PrimeNumbers(object):
    def __init__(self,start,end):
        self.start=start
        self.end=end

    def isPrimeNumber(self,k):
        for i in range(2,k):
            if k%i==0:
                return False
        return True

    def __iter__(self):
        yield '<div class="whole">title</div>'
        yield '<div class="others">'

for x in PrimeNumbers(1,10):
    print(x)






