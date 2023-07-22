class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print('{} is eating'.format(self.name))

    def run(self):
        print('{} is running'.format(self.name))


P1 = Person('张三',22)
P1.eat()
P1.run()