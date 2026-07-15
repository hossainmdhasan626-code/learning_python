# Python _init_() Method

# All classes have a built-in method called __init__(), which is always executed when the class is being initiated.
# The __init__() method is used to assign values to object properties, or to perform operations that are necessary when the object is being created.

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    

p_1 = Person("Hasan",19)
print(p_1.name)
print(p_1.age)

# Note: The __init__() method is called automatically every time the class is being used to create a new object.


print("***")


class Person_1:
    def __init__(self,name,city,age=20): # Default values set kora jabe 
        self.name = name
        self.age = age
        self.city = city
    

p_1 = Person_1("Hasan",age=22,city="N-gong") # Keyword Arguments
print(p_1.name)
print(p_1.age)
print(p_1.city)