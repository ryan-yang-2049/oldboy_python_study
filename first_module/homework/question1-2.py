#q1 请用代码实现：利用下划线将列表的每一个元素拼接成字符串， li = ['alex','eric','rain']

li = ['alex','eric','rain']
res = '_'.join(li)
print(res)

#q2 查找列表中元素，移除每个元素的空格，并查找以a或A开头并且以c结尾的所有元素。
li = ["      alec      ", " aric", "Alex", "Tony", "rain"]
tu = ("alec", " aric", "Alex", "Tony", "rain")
dic = {'k1': "alex", 'k2': ' aric', "k3": "Alex", "k4": "Tony"}

for i in range(len(li)):
    li[i] = li[i].strip()
print(li)

temp_list = []
for i in range(len(tu)):
    res = tu[i].strip()
    temp_list.append(res)
tu = tuple(temp_list)
print(tu,type(tu))

for i in li:
    res = i.strip()
    if res.startswith('a') and res.endswith('c'):
        print(res)
for value in dic.values():
    res = value.strip()
    if res.startswith('a') and res.endswith('c'):
        print(res)





