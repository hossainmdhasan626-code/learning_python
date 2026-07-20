import math

# Python - Math 

# Python has a set of built-in math functions, including an extensive math module, that allows you to perform mathematical tasks on numbers.


# Built-in Math Functions

# The min() and max() functions can be used to find the lowest or highest value in an iterable:

a = min(5,10,11)
b = max(11,55555,2)

print(a)
print(b)


print("***")


# abs()

# The min() and max() functions can be used to find the lowest or highest value in an iterable:
c = abs(-444)
# এটির ভেতর আপনি মাইনাস ওয়ালা কোনো সংখ্যা দিলে সে মাইনাস চিহ্নটাকে কেটে দিয়ে ওটাকে প্লাস (পজিটিভ) বানিয়ে দেয়। আর প্লাস সংখ্যা দিলে সেটা প্লাসই থাকে।
print(c)


print("***")


# pow()

# The pow(x, y) function returns the value of x to the power of y (xy).
d = pow(5,2)
e = pow(5,3)
print(d)
print(e)


print("***")


# The Math Module

# Python has also a built-in module called math, which extends the list of mathematical functions.
# To use it, you must import the math module:

# math.sqrt()

# The math.sqrt() method for example, returns the square root of a number:
x = math.sqrt(25)
print(x)


print("***")


# The math.ceil() method rounds a number upwards to its nearest integer, and the math.floor() method rounds a number downwards to its nearest integer, and returns the result:

f = math.ceil(1.4) #  method rounds a number upwards to its nearest integer,
g = math.floor(1.4) # method rounds a number downwards to its nearest integer

print(f)
print(g)


print("***")


# math.pi

# The math.pi constant, returns the value of PI (3.14...):

x = math.pi
print(x)
