# Basically like javascipt objects
# 'self' is like Javascipt 'this'


class Point:
    # this is like an class constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print('move')

    def draw(self):
        print('draw')


point2 = Point(20, 10)
point2.move()
point2.draw()

# These new properties do not affect other instiatied objects
point2.x = 20
point2.y = 10


# Exercise
class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'Hello! I am {self.name}')


eve = Person('Eve')

eve.talk()
print(eve.name)

# You can also extend from other classes


class Mammal:
    def walk(self):
        print("walk walk")


class Cat(Mammal):
    def speak(self):
        print("meow meow")


bitey = Cat()
bitey.walk()
bitey.speak()


class Dog(Mammal):
 # Python will complain if you define something but add something so just add pass if there is nothing else to define on the claass
    pass


rover = Dog()
rover.walk()
