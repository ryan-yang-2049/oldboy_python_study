# #item系列,类似于字典的操作。
# class Foo: #Dict
#     def __init__(self,name):
#         self.name=name
#
#     def __getitem__(self, item): #item='namexxx'
#         # print('getitem...')
#         return self.__dict__.get(item)
#
#     def __setitem__(self, key, value):
#         # print('setitem...')
#         # print(key,value)
#         self.__dict__[key]=value
#
#     def __delitem__(self, key):
#         # print('delitem...')
#         # print(key)
#         del self.__dict__[key]
#
# obj=Foo('egon')
# print(obj.__dict__)
#
# # 查看属性：
# # obj.属性名
# print(obj['namexxx']) #obj.name
# print(obj['name']) #obj.name
#
# # 设置属性：
# obj['sex']='male'   # 等同于 obj.sex='male'
# print("__dict__:",obj.__dict__)
# print("sex:",obj.sex)
#
# # 删除属性
# del obj['name']     #等同于 del obj.name
# print(obj.__dict__)





#__str__方法：  触发打印操作，直接这个方法下面的内容。
# d=dict({'name':'egon'})
# print(isinstance(d,dict))
# print(d)


class People:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        # print('====>str')
        return '<name:%s,age:%s>' %(self.name,self.age)

obj=People('egon',18)
print(obj) #res=obj.__str__()


#__del__

# f=open('settings.py')
# f.read()
# f.close() #回收操作系统的资源

# print(f)
# f.read()


#
# class Open:
#     def __init__(self,filename):
#         print('open file.......')
#         self.filename=filename
#
#     def __del__(self):              #python程序结束之前就会自动执行。如果提前手动调用则程序结束之前不自动调用
#         print('回收操作系统资源：self.close()')
#
# f=Open('settings.py')
# # del f #f.__del__()
# print('----main------') #del f #f.__del__()



