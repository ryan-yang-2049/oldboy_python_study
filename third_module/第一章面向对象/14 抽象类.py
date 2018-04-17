import abc
class Animal(metaclass=abc.ABCMeta): #只能被继承，不能被实例化
    all_type='animal'

    @abc.abstractmethod
    def run(self):                  #之定义名字，不实现代码
        pass
    @abc.abstractmethod
    def eat(self):
        pass

# animal=Animal()       #这里调用会报错 TypeError，抽象类只能被继承不能被调用

class People(Animal):
    def run(self):
        print('people is running')
    def eat(self):
        print('people is eating')
    def sleep(self):
        print('people is sleep')

class Pig(Animal):
    def run(self):
        print('people is walking')
    def eat(self):
        print('people is eating')

class Dog(Animal):
    def run(self):
        print('people is walking')

    def eat(self):
        print('people is eating')


peo1=People()
pig1=Pig()
dog1=Dog()

peo1.eat()
pig1.eat()
dog1.eat()

print(peo1.all_type)
peo1.sleep()
print(peo1.all_type)
















































