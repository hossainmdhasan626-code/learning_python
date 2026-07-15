# Python self Parameter

# The self parameter is a reference to the current instance of the class.
# It is used to access properties and methods that belong to the class.

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greet(self): # Note: The self parameter must be the first parameter of any method in the class.
        print(f"Hello , my name is {self.name}")


p_1 = Person("Hasan",19)
p_1.greet()


print("***")


# self Does Not Have to Be Named "self"

# It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any method in the class:


class Person_1:
    def __init__(my_object,name,age):
        my_object.name = name 
        my_object.age = age 

    def greet(abc):
        print(f"Hello , my name is {abc.name}")


p_2 = Person_1("Mudra000",33)
p_2.greet()

# Note: While you can use a different name, it is strongly recommended to use self as it is the convention in Python and makes your code more readable to others.

