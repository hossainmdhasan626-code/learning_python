# Multiple Values


# Many Values to Multiple Variables

x,y,z = "mudra000","mahmudul","hasan"
# Python allows you to assign values to multiple variables in one line:
# Note: Make sure the number of variables matches the number of values, or else you will get an error.
print(x)
print(y)
print(z)


# One Value to Multiple Variables

a = b = c = d = "mim"

print(a)
print(b)
print(c)
print(d)


# Unpack a Collection


# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x1, y1, z1 = fruits
print(x1)
print(y1)
print(z1)
# There is a strict rule to follow when unpacking—there must be as many variables to the left of the equal sign as there are elements 
# inside the box. If you give 3 elements and 2 or 4 variables, Python will immediately stop the code with a ValueError 
# (Too many values ​​to unpack or Not enough values ​​to unpack).

# Advanced unpacking

fruits = ["apple", "banana", "cherry", "strawberry", "raspberry"]

# cherry, strawberry, raspberry সবগুলো মিলে 'others' নামের একটি লিস্ট হয়ে যাবে
green, yellow, *others = fruits

print(green)  # apple
print(yellow) # banana
print(others) # ['cherry', 'strawberry', 'raspberry']
# Suppose you have 5 elements in your list, but only 3 variables. In this situation, Python has a magic trick called Asterisk (*) Unpacking.
# If you start any variable name with an asterisk (*), Python will create a new list and insert all the remaining elements into that variable.

fruits = ["apple", "banana", "cherry", "strawberry", "raspberry"]


first, *mid_fruits, last = fruits

print(first)      # apple
print(mid_fruits) # ['banana', 'cherry', 'strawberry']
print(last)       # raspberry

# If the asterisk (*) is in the middle, Python is so smart that if you put the asterisk in the middle, it will combine the first and 
# last elements and put all the remaining middle pieces inside that asterisk: