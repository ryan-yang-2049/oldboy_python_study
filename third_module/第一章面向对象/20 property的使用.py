'''
BMI指数（bmi是计算而来的，但很明显它听起来像是一个属性而非方法，如果我们将其做成一个属性，更便于理解）
成人的BMI数值：过轻：低于18.5;正常：18.5-23.9;过重：24-27;肥胖：28-32;非常肥胖, 高于32
体质指数（BMI）=体重（kg）÷身高^2（m）
EX：70kg÷（1.75×1.75）=22.86
'''
# class People:
#     def __init__(self,name,weight,height):
#         self.name=name
#         self.weight=weight
#         self.height=height
#
#     @property
#     def bmi(self):
#         return self.weight / (self.height ** 2)
#
# p=People('cherry',65,1.73)
# # p.bmi=p.weight / (p.height ** 2)
# print(p.bmi)
#
# # print(p.bmi())
# # print(p.bmi)
#
# p.height=1.82
# print(p.bmi)
#
# p.bmi=3333 #报错AttributeError: can't set attribute

#property 可以封装一些通过计算后，在访问的数据类型等封装在函数里面，通过 “对象.属性” 访问。


class People:
    def __init__(self,name):
        self.__name=name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,val):
        if not isinstance(val,str):
            print('名字必须是字符串类型')
            return
        self.__name=val

    @name.deleter
    def name(self):
        print('不允许删除')


p=People('egon')


print("1)打印name：",p.name)

p.name='EGON'
p.name=123
print("2)打印name",p.name)

del p.name









