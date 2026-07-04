# Python - Function 


# Python Functions

# A function is a block of code which only runs when it is called.
# A function can return data as a result.
# A function helps avoiding code repetition.


# Creating a Function
# In Python, a function is defined using the def keyword, followed by a function name and parentheses:

def my_function():
    print("Hello, World!") # The code inside the function must be indented. Python uses indentation to define code blocks.
# This creates a function named my_function that prints "Hello from a function" when called.


# Now Calling a Function
my_function()
# To call a function, write its name followed by parentheses:

# You can call the same function multiple times:
my_function()
my_function()
my_function()


print("***")


# Function Names
# ***
# Function names follow the same rules as variable names in Python:
# A function name must start with a letter or underscore
# A function name can only contain letters, numbers, and underscores
# Function names are case-sensitive (myFunction and myfunction are different)
# ***


print("***")


# Return Values

# Functions can send data back to the code that called them using the return statement.
# When a function reaches a return statement, it stops executing and sends the result back:
def get_return():
    return "Hello World" # *** If a function doesn't have a return statement, it returns None by default.
print(get_return())


print("***")


# The pass Statement
# Function definitions cannot be empty. If you need to create a function placeholder without any code, use the pass statement:
def my_pass():
    pass