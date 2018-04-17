'''
3,写代码，有如下列表，按照要求实现每一个功能 li = ['alex','eric','rain']
'''
li = ['alex','eric','rain']
#q1
length = len(li)

#q2
li.append('seven')
print(li)

#q3
li.insert(1,"Tony")
print(li)

#q4
li[2] = 'Kelly'
print(li)

# #q5
# li.remove('eric')
# print(li)

#q6
li = ['alex','eric','rain']
res = li.pop()
print(res,li)

#q7
li = ['alex', 'eric', 'rain','seven']
li.remove(li[3])
print(li)
#q8
li = ['alex', 'Tony', 'eric','Kelly', 'rain', 'seven']
res = li[2:5]
for i in res:
    li.remove(i)
print(li)

#q9
li = ['alex', 'Tony', 'eric','Kelly', 'rain', 'seven']
li.reverse()
print(li)

#q10
# for i in range(len(li)):
#     print(i)

#q10

for key,value in enumerate(li,100):
    print(key,value)

for i in li:
    print(i)
