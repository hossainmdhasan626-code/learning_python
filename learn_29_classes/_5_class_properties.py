# Python Class Properties


# Class Properties 

# Properties are variables that belong to a class. They store data for each object created from the class.

class Person:
    def __init__(self,name,age):
        self.name = name # Properties
        self.age = age # Properties

p_1 = Person("Mudra000",33)
print(p_1.name) # Access Properties
print(p_1.age) # Access Properties


print("***")


# Modify Properties
# You can modify the value of properties on objects:

class Person_1:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p_2 = Person_1("Md h", 44)
print(p_2.age) 

# Modify the ages value
p_2.age = 33
print(p_2.age)