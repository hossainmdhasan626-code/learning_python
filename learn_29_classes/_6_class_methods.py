# Python Class Methods 


# Class Methods

# Methods are functions that belong to a class. They define the behavior of objects created from the class.
class Person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age 

    def greet(self): # Etai ekta method() . Note: All methods must have self as the first parameter.

        print(f"Hello, my name is {self.name}")

p_1 = Person("mudra000",19)
p_1.greet() # Ekhane method() ke call kora hocche 


print("***")


class Calculator:
    def add(self,a,b):
        return a + b 
    def multiply(self,a,b):
        return a * b 

cal = Calculator()
print(cal.add(5,5))
print(cal.multiply(4,4))