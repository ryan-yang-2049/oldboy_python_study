#在子类派生出的新的方法中重用父类的方法，有两种实现方式
#方式一：指名道姓（不依赖继承）
# class Hero:
#     def __init__(self,nickname,life_value,aggresivity):
#         self.nickname=nickname
#         self.life_value=life_value
#         self.aggresivity=aggresivity
#     def attack(self,enemy):
#         enemy.life_value-=self.aggresivity
#
#
# class Garen(Hero):
#     camp='Demacia'
#
#     def attack(self,enemy):
#         Hero.attack(self,enemy) #指名道姓，不以来继承，相当于用了另外一个类的方法。
#         print('from Garen Class')
#
# class Riven(Hero):
#     camp='Noxus'
#
#
# g=Garen('草丛伦',100,30)
# r=Riven('锐雯雯',80,50)
#
# print(r.life_value)
# g.attack(r)
# print(r.life_value)



#
# class Hero:
#     def __init__(self,nickname,life_value,aggresivity):
#         self.nickname=nickname
#         self.life_value=life_value
#         self.aggresivity=aggresivity
#     def attack(self,enemy):
#         enemy.life_value-=self.aggresivity
#
#
# class Garen(Hero):
#     camp='Demacia'
#
#     def __init__(self,nickname,life_value,aggresivity,weapon):
#         # self.nickname=nickname
#         # self.life_value=life_value
#         # self.aggresivity=aggresivity
#         Hero.__init__(self,nickname,life_value,aggresivity)
#         self.weapon=weapon
#
#     def attack(self,enemy):
#         Hero.attack(self,enemy) #指名道姓
#         print('from Garen Class')
#
#
# g=Garen('草丛伦',100,30,'金箍棒')
# print(g.__dict__)




#方式二：super() (依赖继承)
# class Hero:
#     def __init__(self,nickname,life_value,aggresivity):
#         self.nickname=nickname
#         self.life_value=life_value
#         self.aggresivity=aggresivity
#     def attack(self,enemy):
#         enemy.life_value-=self.aggresivity
#
#
# class Garen(Hero):
#     camp='Demacia'
#
#     def attack(self,enemy):
#         super(Garen,self).attack(enemy) #依赖继承
#         print('from Garen Class')
#
# class Riven(Hero):
#     camp='Noxus'
#
#
# g=Garen('草丛伦',100,30)
# r=Riven('锐雯雯',80,50)
#
# g.attack(r)
# print(r.life_value)
#
#
# class Hero:
#     def __init__(self,nickname,life_value,aggresivity):
#         self.nickname=nickname
#         self.life_value=life_value
#         self.aggresivity=aggresivity
#     def attack(self,enemy):
#         enemy.life_value-=self.aggresivity
#
# class Garen(Hero):
#     camp='Demacia'
#
#     def __init__(self,nickname,life_value,aggresivity,weapon):
#         # super(Garen,self).__init__(nickname,life_value,aggresivity)
#         super().__init__(nickname,life_value,aggresivity)   #super qu mro中找
#         self.weapon=weapon
#
#     def attack(self,enemy):
#         super().attack(enemy)  #实际上是这样用的 super(Garen,self).attack(enemy)
#         print('from Garen Class')
# class Riven(Hero):
#     camp='Noxus'
#
#
#
# g=Garen('草丛伦',200,50,'金箍棒')
# print(Garen.__mro__)
# print(g.__dict__)
#
# r=Riven('锐雯雯',80,50)
# g.attack(r)
# print(r.life_value)
#






class A:
    def f1(self):
        print('from A')
        super().f1()        #此时位置在mro列表中的 class_A 位置，因为super会沿着 mro列表往后找，因此，会找到class_B

class B:
    def f1(self):
        print('from B')

class C(A,B):
    pass

#
print(C.mro())
c=C()
c.f1()









