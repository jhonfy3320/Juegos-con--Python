from pyclbr import Class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f'Hola, mi nombres es {self.name} y mi edad es {self.age}')
    
person1 = Person('Nicolas', 13)
person2 = Person('Alejandro', 12)
person3 = Person('Freddy', 32)

person1.greet()
person2.greet()
person3.greet()