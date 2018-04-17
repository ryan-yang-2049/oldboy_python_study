'''
在现实世界中：
    对象1：王二丫
        特征：
            学校='luffycity'
            名字='王二丫'
            性别='女'
            年龄=18
        技能：
            学习
            吃饭
            睡觉

    对象2：李三炮
        特征：
            学校='luffycity'
            名字='李三炮'
            性别='男'
            年龄=38
        技能：
            学习
            吃饭
            睡觉

'''
x='global'
class LuffyStudent:
    school='luffycity'

    def __init__(self,name,sex,age):
        self.Name=name
        self.Sex=sex
        self.Age=age

    def learn(self,x):
        print('%s is learning %s' %(self.Name,x))

    def eat(self):
        print('%s is sleeping' %self.Name)


#后产生对象
stu1=LuffyStudent('王二丫','女',18)
stu2=LuffyStudent('李三炮','男',38)
stu3=LuffyStudent('张铁蛋','男',48)
# print(stu1.__dict__)
# print(stu2.__dict__)
# print(stu3.__dict__)



#对象：特征与技能的结合体
#类：类是一系列对象相似的特征与相似的技能的结合体



#类中的数据属性：是所以对象共有的(实例化对象和包括类本身)
# print(LuffyStudent.school,id(LuffyStudent.school))
#
# print(stu1.school,id(stu1.school))
# print(stu2.school,id(stu2.school))
# print(stu3.school,id(stu3.school))


#类中的函数属性:是绑定给对象使用的，绑定到不同的对象是不同的绑定方法，对象调用绑定方式时，会把对象本身当作第一个传入，传给self

# print(LuffyStudent.learn)
# LuffyStudent.learn(stu1)
# LuffyStudent.learn(stu2)
# LuffyStudent.learn(stu3)


# print(stu1.learn)
# stu1.learn(1) #LuffyStudent.learn(stu1,1)
# print(stu2.learn)



# stu2.learn(2)
# stu3.learn(3)



#先从自己的名称空间里面找自己的属性，然后在从类里面找属性，类里面没有直接报错。
stu1.x='from stu1'
LuffyStudent.x='from Luffycity class'
print(LuffyStudent.__dict__)
print(stu1.__dict__)
print("属性：",stu1.x)












