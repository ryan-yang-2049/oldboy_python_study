'''question 9'''

li = [11,22,33,44,55,66,77,88,99,90]
dic = {}
v1 = []
v2 = []
for value in li:
    if value > 66:
        v1.append(value)
        dic.setdefault('k1',v1)
    else:
        v2.append(value)
        dic.setdefault('k2',v2)
print(dic)




