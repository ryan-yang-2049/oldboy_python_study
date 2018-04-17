#_*_coding:utf-8_*_


#f = open(file="兼职白领学生空姐模特护士联系方式.txt", mode="rb",encoding="gbk")
f = open(file="兼职白领学生空姐模特护士联系方式utf8.txt", mode="r")

# data = f.read()
for line in f:
    print(line)
f.close()