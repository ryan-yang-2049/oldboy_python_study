#先定义类
class LuffyStudent:
    school='luffycity' #数据属性


    def learn(self): #函数属性
        print('is learning')

    def eat(self): #函数属性
        print('is sleeping')

# 类是，一系列对象相似特征与技能的结合体
# 特征用变量去表示，技能用函数去表示。
# 查看类的名称空间
# print(LuffyStudent.__dict__)            #打印类的名称空间
# print(LuffyStudent.__dict__['school'])  #打印数据属性的名称空间
# print(LuffyStudent.__dict__['learn'])   #打印方法（函数，技能）的名称空间


# #查
# print(LuffyStudent.school) #LuffyStudent.__dict__['school']
# print(LuffyStudent.learn) #LuffyStudent.__dict__['learn']

#增
LuffyStudent.county='China'
# print(LuffyStudent.__dict__)
# print(LuffyStudent.county)

# 删
del LuffyStudent.county

# 改
LuffyStudent.school='Luffycity'
print(LuffyStudent.school)
