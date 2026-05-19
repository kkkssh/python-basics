# =========================
# CLASSES & OBJECTS
# =========================

# object-oriented programming (OOP) is a programming style
# where related data and functionality are grouped together
# inside objects

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


# OBJECT METHODS WITH LISTS
class Pie:
    def __init__(self, flavor, ingredients):
        self.flavor = flavor
        self.ingredients = ingredients
        self.num_ingredients = len(ingredients)

    def print_ingredients(self):
        for i in self.ingredients:
            print(i)

apple_pie = Pie("apple", ["flour", "eggs", "apples", "butter"])

apple_pie.print_ingredients()
print(apple_pie.num_ingredients)


# INSTANCE VARIABLES VS CLASS VARIABLES
class Student:
    school = "Oxford"   # class variable

    def __init__(self, name):
        self.name = name    # instance variable


student1 = Student("Chloe")
student2 = Student("James")

print(student1.school)
print(student2.school)

print(student1.name)
print(student2.name)


# FUNCTIONAL PROGRAMMING VS OBJECT-ORIENTED PROGRAMMING

# Functional programming organizes code using functions 
# Object-oriented programming organizes code using objects and classes


# Functional style
def introduce_student(name, major):
    return f"{name} studies {major}."

print(introduce_student("Chloe", "Business"))


# Object-oriented style
class UniversityStudent:
    def __init__(self, name, major):
        self.name = name
        self.major = major

    def introduce(self):
        return f"{self.name} studies {self.major}."

student = UniversityStudent("Chloe", "Business")
print(student.introduce())


# INHERITANCE

# inheritance allows a child class to inherit attributes and methods from a parent class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hi!")


class ScienceStudent(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major

    def intro(self):
        print(f"My name is {self.name}")
        print(f"My major is {self.major}")


student = ScienceStudent("Sam", 23, "Chemistry")

print(student.age)
print(student.major)

student.greet()
student.intro()