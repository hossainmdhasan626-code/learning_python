# Python *args and **kwargs

# *args and **kwargs
# By default, a function must be called with the correct number of arguments.
# However, sometimes you may not know how many arguments that will be passed into your function.
# *args and **kwargs allow functions to accept a unknown number of arguments.

def my_function(*args):
    print(sum(args))
my_function(1,2,3,2,5,6,4444,22,2456)


print("***")


# What is *args?

# The *args parameter allows a function to accept any number of positional arguments.
# Inside the function, args becomes a tuple containing all the passed arguments:
def my_function_1(*args):
    print(f"Type: {type(args)}")
    print(f"First argument : {args[0]}")
    print(f"second argument : {args[1]}")
    print(f"All arguments : {args}")

my_function_1("Emili","Jackson","Mother-teresha","Lakhi begum")


print("***")


# Arbitrary Keyword Arguments - **kwargs

# If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name.
# This way, the function will receive a dictionary of arguments and can access the items accordingly:
def my_function_2(**kwargs):
    print(f"His last name is {kwargs["lname"]}")
my_function_2(fname = "Md Mahmudul", lname = "Hasan")