
class Humanity(object):

    def __init__(self,name,sex):
        self.name = name
        self.sex = sex





class Teacher(Humanity):

    def __init__(self,name,sex,salary):

        super(Teacher,self).__init__(name,sex)
        self.salary = salary
        self.teach_class = {}

    def teach_info(self,class_name,course_name):
        self.teach_class[class_name] = course_name




class Student(Humanity):

    def __init__(self,name,sex,school, class_name):
        super(Student, self).__init__(name, sex)
        self.school = school
        self.class_name = class_name


# tea1 = Teacher('ryan','man',18,'300')
# tea1.teach_info('L1','Python')
# print(tea1.__dict__)