# Python - None


# NoneType
# Variables can be assigned None to indicate "no value" or "not set".
a = None
print(a)


print("***")


# Use type() to see the type of a None value.
print(type(a))


print("***")


# Comparing to None

# To compare a value to None, use the identity operator is or is not

b = None
if b is None:
    print("No result yet")
else:
    print("Result is ready")


print("***")


if b is not None:
    print("Result is readdy")
else:
    print("No result yet")



print("***")



print(bool(None))


print("***")


# Functions returning None

# Functions that do not explicitly return a value return None by default.

def my_function():
    x = 5 

x = my_function()
print(x)