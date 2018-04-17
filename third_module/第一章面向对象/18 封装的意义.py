#一：封装数据属性：明确的区分内外，控制外部对隐藏的属性的操作行为
# class People:
#     def __init__(self,name,age):
#         self.__name=name
#         self.__age=age
#
#     def tell_info(self):    #外部查看内部隐藏属性的一个接口
#         print('Name:<%s> Age:<%s>' %(self.__name,self.__age))
#
#     def set_info(self,name,age):    #外部修改内部隐藏属性一个接口
#         if not isinstance(name,str):    #对修改属性时，进行值的判断
#             print('名字必须是字符串类型')
#             return
#         if not isinstance(age,int):     #对修改属性时，进行值的判断
#             print('年龄必须是数字类型')
#             return
#         self.__name=name
#         self.__age=age
#
# p=People('egon',18)
#
# p.tell_info()   #查看内部隐藏属性
#
# p.set_info('Ryan',28)
# p.tell_info()

# p.set_info(123,38)
# p.set_info('egon','38')
# p.tell_info()


#二、 封装方法：隔离复杂度

class ATM:
    def __card(self):
        print('插卡')
    def __auth(self):
        print('用户认证')
    def __input(self):
        print('输入取款金额')
    def __print_bill(self):
        print('打印账单')
    def __take_money(self):
        print('取款')

    def withdraw(self):
        self.__card()
        self.__auth()
        self.__input()
        self.__print_bill()
        self.__take_money()

a=ATM()

a.withdraw()





















