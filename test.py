import random


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    num = random.randint(1, 10)

    def eat(self):
        print('{} is eating'.format(self.name))
        print('你的年龄是{}'.format(self.age))

    def run(self, num):
        print('{} is running'.format(self.name))


P1 = Person('张三',22)
P1.eat()
P1.run(2)