# =========================
# CLASSES & OBJECTS
# =========================

# a class is a blueprint for creating objects

# attributes are variables that belong to an object

# methods are functions inside a class

# self refers to the current object itself
# it allows each object to store its own data

# __init__ is a constructor method
# it runs automatically when an object is created

# class variables are shared by all objects


# BASIC CLASS EXAMPLE
class Dog:
    def __init__(self, name, age):  
        self.name = name
        self.age = age

    def bark(self):    
        print(f"{self.name} says woof!")


dog1 = Dog("Milo", 3)

print(dog1.name)
dog1.bark()


# CLASS VARIABLES
class OlympicSports:
    name = "Gymnastics"
    countries = ["USA", "UK", "Japan"]

gymnastics = OlympicSports()
print(gymnastics.countries[0])


# MULTIPLE OBJECTS
class Computer:
    def __init__(self, size, storage):  
        self.size = size
        self.storage = storage

    def print_specs(self):      
        print(f"Display size: {self.size}")
        print(f"Storage size: {self.storage}")

low_spec = Computer("13-inch", "256GB")
high_spec = Computer("27-inch", "1TB")

print("Low Spec Computer")
low_spec.print_specs()

print()

print("High Spec Computer")
high_spec.print_specs()