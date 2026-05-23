# =========================
# ADVANCED OBJECT-ORIENTED PROGRAMMING
# =========================

# abstraction hides internal implementation and shows only essential functionality

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