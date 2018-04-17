'''转换'''
s = 'alex'
li01 = list(s)
print(li01)

tup01 = tuple(s)
print(tup01)

li = ['alex','seven']
li =tuple(li)
print(li,type(li))


tu = ('Alex','seven')
tu = list(tu)
print(tu,type(tu))

li = ["alex","seven"]
li_key = []
for i in list(range(len(li))):
    # li_key[i] += 10
    i += 10
    li_key.append(i)
dic = dict(zip(li_key,li))
print(dic)

