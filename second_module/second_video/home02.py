#coding:utf-8


import io



list01 = []
read_file = io.open("name.txt",'r+',encoding="utf-8")

for line in read_file.readlines():
        line = line.strip('\n')
        line = line+'\n'
        list01.append(line)

list01.append("10 ryan\n")

values = ''.join(list01)
read_file.seek(0)
read_file.write(values)
read_file.truncate()

read_file.seek(0)
for line in read_file.readlines():
    line = line.split()[1]
    print(line)


read_file.close()

