# class ParentClass1:
#     pass
#
# class ParentClass2:
#     pass
#
# class SubClass1(ParentClass1):
#     pass
#
# class SubClass2(ParentClass1,ParentClass2):
#     pass
#
# print(SubClass1.__bases__)   #查看继承的父类
# print(SubClass2.__bases__)
#
#
# print(ParentClass1.__bases__)
# class Hero:
#     x=3
#     def __init__(self,nickname,life_value,aggresivity):
#         self.nickname=nickname
#         self.life_value=life_value
#         self.aggresivity=aggresivity
#     def attack(self,enemy):
#         enemy.life_value-=self.aggresivity
#
# class Garen(Hero):
#     x=2
#     pass
#
# class Riven(Hero):
#     pass
#
#
# g1=Garen('刚们',29,30)
# # print(g1.nickname,g1.life_value,g1.aggresivity)
# # g1.x=1
#
# print(g1.x)



#属性查找小练习
class Foo:
    def f1(self):
        print('from Foo.f1')

    def f2(self):
        print('from Foo.f2')
        self.f1() # self 现在是 b的对象，然后 得到 b.f1()，那么又从对象b本身开始找

class Bar(Foo):
    def f1(self):
        print('from Bar.f1')

b=Bar()
print(b.__dict__)   #查看对象本身的 __init__ 方法
b.f2()



