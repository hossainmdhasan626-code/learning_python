# Python - Function Lambda

# Lambda Functions

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

# Syntax

# lambda arguments : expression

x = lambda a : a + 10
print(x(5))


print("***")


# Lambda functions can take any number of arguments:

x_1 = lambda a,b : a + b 
print(x_1(6,10))

x_2 = lambda *x : sum(x)
print(x_2(5,5,5,5,444,35437,444,))


print("***")


# Why Use Lambda Functions?
