# Global Variables

# Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.
# Global variables can be used by everyone, both inside of functions and outside.

x = "awesome"

def myfun():
    print("Pythone is", x)
    print("Pythone is" + x) # Pythone isawesome

myfun()


# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. 
# The global variable with the same name will remain as it was, global and with the original value.

x1 = "awesome"

def myfun():
    x1 = "fantastic"
    print("Pythone is" , x1)

myfun()

print("Pythone is" , x1)


# The global Keyword

# Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
# To create a global variable inside a function, you can use the global keyword.

# If you use the global keyword, the variable belongs to the global scope:

def myfunc():
  global x2
  x2 = "fantastic"

myfunc()

print("Python is " + x2)

# To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x3 = "awesome"

def myfunc():
  global x3
  x3 = "fantastic"

myfunc()

print("Python is " + x3)
