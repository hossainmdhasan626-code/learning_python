# Python Classes and Objects 


# Python Classes/Objects

# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.


# Create a Class

# To create a class, use the keyword class
class Myclass:
    x = 5
print(Myclass)

print("***")


# Create Object
# Now we can use the class named MyClass to create objects:
p_1 = Myclass()
print(p_1.x)


print("***")


# Multiple Objects

# You can create multiple objects from the same class:
p_2 = Myclass()
p_3 = Myclass()

print(p_2.x)
print("***")
print(p_3.x)
# Note: Each object is independent and has its own copy of the class properties.


# The pass Statement
# class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

