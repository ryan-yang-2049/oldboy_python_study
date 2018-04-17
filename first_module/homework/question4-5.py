
'''
question4
'''

li = ["hello", 'seven', ["mon", ["h", "kelly"], 'all'], 123, 446]
res = li[2][1][1]
print(res)

li[2][2] = 'All'
print(li)

#question5
tu = ('alex', 'eric', 'rain')
print(len(tu))
print(tu[2])
print(tu[0:2])

for i in tu:
    print(i)


for i in range(len(tu)):
    print(i,tu[i])

for key,value in enumerate(tu):
    print(key,'-->',value)
