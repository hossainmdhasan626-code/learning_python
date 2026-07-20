# Python Encapsulation

# Encapsulation is about protecting data inside a class.
# It means keeping data (properties) and methods together in a class, while controlling how the data can be accessed from outside the class.
# This prevents accidental changes to your data and hides the internal details of how your class works.


# Private Properties
# In Python, you can make properties private by using a double underscore __ prefix:

class Person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age # Private property

p_1 = Person("Emil",25)
print(p_1.name)
# print(p_1.__age) # Note: Private properties cannot be accessed directly from outside the class.


print("***")


# Get Private Property Value

# To access a private property, you can create a getter method:

class Person_1:
    def __init__(self,name,age):
        self.name = name 
        self.__age = age 

    def get_age(self):
        return self.__age
    
p_2 = Person_1("Toba",33)
print(p_2.get_age())