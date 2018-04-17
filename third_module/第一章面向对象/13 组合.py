class People:
    school='luffycity'
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

class Teacher(People):
    def __init__(self,name,age,sex,level,salary,):
        super().__init__(name,age,sex)
        self.level=level
        self.salary=salary

    def teach(self):
        print('%s is teaching' %self.name)

class Student(People):
    def __init__(self, name, age, sex, class_time,):
        super().__init__(name,age,sex)
        self.class_time=class_time
    def learn(self):
        print('%s is learning' % self.name)

class Course:
    def __init__(self,course_name,course_price,course_period):
        self.course_name = course_name
        self.course_price = course_price
        self.course_period = course_period
    def tell_info(self):
        print('课程名<%s> 课程价钱<%s> 课程周期<%s>' %(self.course_name,self.course_price,self.course_period))

class Date:
    def __init__(self,year,mon,day):
        self.year=year
        self.mon=mon
        self.day=day

    def tell_info(self):
        print('%s-%s-%s' %(self.year,self.mon,self.day))

# teacher1=Teacher('alex',18,'male',10,3000,)     # 实例化教师1对象
# teacher2=Teacher('egon',28,'male',30,3000,)     # 实例化教师2对象
# python=Course('python',3000,'3mons')            # 实例化课程对象
# linux=Course('linux',2000,'4mons')              # 实例化课程对象
#
# teacher1.course=python                          #相当于给教师1，添加一个属性
# teacher2.course=python                          #相当于给教师1，添加一个属性

# print("实例化的对象：",python)
# print("实例化对象的属性",python.course_name)
# print("教师1的课程对象：",teacher1.course)
# print("教师2的课程对象：",teacher2.course)
# print("教师1的课程名称：",teacher1.course.course_name)
# print("教师2的课程名称：",teacher2.course.course_name)
# teacher1.course.tell_info()
# print(teacher1.course.__dict__)

# student1=Student('张三',28,'female','08:30:00')  # 实例化一个student1的对象
# python=Course('python',3000,'3mons')            # 实例化课程对象
# linux=Course('linux',2000,'4mons')              # 实例化课程对象
# student1.course1=python                         # 给学生添加了一个python课程属性
# student1.course2=linux                          # 给学生添加了一个linux课程的属性

# student1.course1.tell_info()
# student1.course2.tell_info()

# student1.courses=[]
# student1.courses.append(python)
# student1.courses.append(linux)
#
# for num in range(len(student1.courses)):
#     # print(student1.courses[num].__dict__)
#     # print(student1.courses[num].course_name)
#     student1.courses[num].tell_info()



student1=Student('张三',28,'female','08:30:00')
d=Date(1988,4,20)
python=Course('python',3000,'3mons')


student1.birh=d
student1.birh.tell_info()

student1.course=python

student1.course.tell_info()
















