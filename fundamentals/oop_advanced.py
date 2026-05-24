# =========================
# ADVANCED OBJECT-ORIENTED PROGRAMMING
# =========================

# abstraction hides internal implementation 
# and shows only essential functionality

class Car:
    def __init__(self):
        self.on = False

    def inject_fuel(self):
        print("Spraying fuel")

    def ignite_fuel(self):
        print("Boom!")

    def start_up(self):
        self.on = True

        self.inject_fuel()
        self.ignite_fuel()

        print("Car started")


car = Car()
car.start_up()


# =========================
# ABSTRACT CLASSES
# =========================

# ABC stands for Abstract Base Class
# it is used to create abstract classes in Python

# abstractmethod is used to define methods
# that child classes must implement

from abc import ABC, abstractmethod


# Vehicle is an abstract class
# abstract classes cannot create objects directly
class Vehicle(ABC):

    # this method must be implemented
    # by child classes
    @abstractmethod
    def start_up(self):
        pass


# SportsCar inherits from Vehicle
class SportsCar(Vehicle):

    # child class provides its own implementation
    # of the abstract method
    def start_up(self):
        print("Spraying fuel")
        print("Boom!")
        print("Car started")


# create object
car = SportsCar()

# call method
car.start_up()


# =========================
# POLYMORPHISM
# =========================

# polymorphism allows different classes
# to use the same method in different ways

class Feline:
    def speak(self):
        print("Meow")


class Cat(Feline):
    def lick(self):
        print("Licking paw")


class Lion(Feline):
    def prey(self):
        print("Pounces on prey")

    def speak(self):
        print("ROAR!")


cat = Cat()
cat.speak()

lion = Lion()
lion.speak()

# Polymorphism with a loop
animals = [Cat(), Lion()]

for animal in animals:
    animal.speak()


# =========================
# OBJECT STATE AND METHODS
# =========================

# objects can store state
# and update it through methods

class Slideshow:
    def __init__(self, slides):
        self.slides = slides
        self.current = 1

    def view_next_slide(self):
        self.current += 1

    def play(self):
        while self.current <= self.slides:
            print("Slide", self.current)
            self.view_next_slide()


slideshow = Slideshow(5)
slideshow.play()