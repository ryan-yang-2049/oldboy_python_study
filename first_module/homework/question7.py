'''
question 7
'''

dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}

for key in dic.keys():
    print(key)
for value in dic.values():
    print(value)
for key,value in dic.items():
    print(key,value)

dic.setdefault('k4','v4')
print(dic)

dic['k1'] = 'alex'
print(dic)
dic['k3'].append(44)
dic['k3'].insert(1,18)
print(dic)