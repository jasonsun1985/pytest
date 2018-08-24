# coding:utf-8
from com.test.po.animal import Animal


class Dog(Animal):
    '''
    classdocs
    '''

    def __init__(self, params):
        pass

    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')


dog = Dog(object)
dog.run()
print(type(dog))
print(isinstance(dog, Animal))
print(dir(Dog))
print(hasattr(dog,"x"))
