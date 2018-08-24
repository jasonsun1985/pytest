# coding:utf-8
from itertools import count
from builtins import ValueError


class Student(object):
    
    '''
    classdocs
    '''
    count = 0
    def __init__(self, name, scroe, gender):
        '''
        Constructor
        '''
        self.name = name
        self.scroe = scroe
        self.__gender = gender
        Student.count +=1

    def get_grade(self):
        if self.scroe >= 90:
            print("A")
        elif self.scroe >= 60 & self.scroe < 90:
            print("B")
        else:
            print("C")

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender
       
    @property 
    def score(self):
        return self._score
    
    @score.setter
    def score(self,value):
        if not isinstance(value, int):
            raise ValueError("必须为数字")
        if value < 0 or value > 100:
            raise ValueError("数值必须在0~100之间")
        self._score = value
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value
        

if __name__ == '__main__':
    o1 = Student("jason", 98,'male')
    print(o1.name, o1.scroe,o1.get_gender())
    print("%s - %s : %s" % (o1.name, o1.scroe,o1.get_gender()))
bart = Student('Bart',80, 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')
        
for n in range(10):
    Student("jason", 88+n,'male')
print('Student 对象被初始化了  %s 次' % Student.count)

s=Student("jason", 98,'male')
s.score=98
print(s.score)
