#__init__方法用来为对象定制对象自己独有的特征
class LuffyStudent:
    school='luffycity'

    #            stu1,'王二丫','女',18
    def __init__(self,name,sex,age):
        self.Name=name
        self.Sex=sex
        self.Age=age

    def learn(self):
        print('is learning')

    def eat(self):
        print('is sleeping')

# print(LuffyStudent.__dict__)

#后产生对象
stu1=LuffyStudent('王二丫','女',18) #LuffyStudent.__init__(stu1,'王二丫','女',18)
# print(stu1.__dict__)

# 加上__init__方法后，实例化的步骤
# self 相当于 stu1 （实例化的对象的名称）
# 1、先产生一个空对象stu1
# 2、LuffyStudent.__init__(stu1,'王二丫','女',18)


#查
# print(LuffyStudent.__dict__)   #类的名称空间
# print(stu1.__dict__)       #实例化对象自己独有的属性
# print(stu1.Name)
# print(stu1.Sex)
# print(stu1.Age)

#改
# print("未改变对象属性之前:",stu1.__dict__)
# stu1.Name='李二丫'
# print("改变对象属性之后：",stu1.__dict__)
# print(stu1.Name)


#删除
# del stu1.Name
# print(stu1.__dict__)

# #增
stu1.class_name='python开发'
print(stu1.__dict__)
#
#
# stu2=LuffyStudent('李三炮','男',38) #Luffycity.__init__(stu2,'李三炮','男',38)
# print(stu2.__dict__)
# print(stu2.Name)
# print(stu2.Age)
# print(stu2.Sex)