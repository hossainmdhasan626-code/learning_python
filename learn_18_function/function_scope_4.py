# Python Scope 


# Scope

# A variable is only available from inside the region it is created. This is called scope.


# Local Scope
# A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
def my_function():
    x = 30 
    print(x)
my_function()


print("***")


# Function Inside Function

# As explained in the example above, the variable x is not available outside the function, but it is available for any function inside the function:

def my_function():
    x = 30 
    def inner_funciton(): # Inner funciton 
        print(x) # Inner/child function can accece the parent function variable
    inner_funciton()
my_function()


print("***")


# Global Scope

# A variable created in the main body of the Python code is a global variable and belongs to the global scope.
# Global variables are available from within any scope, global and local.
x_1 = 300

def my_function_1():
    print(x_1)
    
my_function_1()


print("***")


# Naming Variables

# If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables, 
# one available in the global scope (outside the function) and one available in the local scope (inside the function):
x_2 = 300

def my_function_2():
    x = 200
    print(x)

my_function_2()
print(x_2)


print("***")


# Global Keyword

# If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
# The global keyword makes the variable global.
def funciton_3():
    global x_3
    x_3 = 400
funciton_3()
print(x_3)


print("***")


# Also, use the global keyword if you want to make a change to a global variable inside a function.
x_4 = 450

def my_function_4():
    global x_4
    x_4 = 500
print(x_4) # globl variable was 450 
my_function_4() # global variable was change to 500
print(x_4) # Now the global variable was 500


print("***")


# Nonlocal Keyword

# সহজ কথায়: আপনি যখন ফাংশনের ভেতর আরেকটা ফাংশন লেখেন, তখন ভেতরের ফাংশন থেকে বাইরের ফাংশনের কোনো ভ্যারিয়েবলকে শুধু "পড়া" (Read) যায়, 
# কিন্তু সরাসরি "বদলানো" (Modify) যায় না। ওই বাইরের ভ্যারিয়েবলটাকে জোর খাটানো বা পরিবর্তন করার লাইসেন্সই হলো nonlocal।
def my_function_5():
    x = "Jane"
    def inner_funciton():
        nonlocal x 
        x = "Hello, World!"
    inner_funciton()
    return x 

print(my_function_5())