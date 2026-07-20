# Outputs Values


# In the print() function, you output multiple variables, separated by a comma:

x = "Python"
y = "is"
z = "awesome"

print(x,y,z)


# You can also use the + operator to output multiple variables:

x1 = "Python"
y1 = "is"
z1 = "awesome"

print(x1 + y1 + z1)

# For numbers, the + character works as a mathematical operator:
x2 = 5
y2 = 10
print(x2 + y2)


# In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:
# x3 = 5
# y3 = "John"
# print(x3 + y3)


# The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:

x4 = 5
y4 = "John"
print(x4, y4)