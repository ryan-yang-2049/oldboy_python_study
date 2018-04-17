#!/usr/bin/env python
#coding:utf-8


# 2. 求100以内不能被3整除的所有数，并把这些数字放在列表sum=[]里，并求出这些数字的总和和平均数
sum = []
count = 0
avg = 0

for i in range(0,101):
    if i%3 == 0:
        continue
    else:
        sum.append(i)

for i in sum:
    count += i


avg = count/len(sum)

print(sum)
print("总和：",count)
print("平均数：",avg)

