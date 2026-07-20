# Python - Function Arguments


# Arguments

# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
def my_function(fname): # A parameter is the variable listed inside the parentheses in the function definition.
    print(fname + " " + "Refsan")
my_function("Email")  #  An argument is the actual value that is sent to the function when it is called.
my_function("Tobias") # An argument is the actual value that is sent to the function when it is called.
my_function("Linus") # An argument is the actual value that is sent to the function when it is called.A parameter is the variable listed inside the parentheses in the function definition.


print("***")


# Number of Arguments

# By default, a function must be called with the correct number of arguments.
# If your function expects 2 arguments, you must call it with exactly 2 arguments.
def my_function_1(fname,lname):
    print(fname + " " + lname)

my_function_1("Md Mahmudul","Hasan")
my_function_1("Mim","Acter")
my_function_1("Taniya","Islam")


print("***")


# Default Parameter Values 

def my_function_2(name = "friend"):
    print("Hello" + " " + name)

my_function_2("Hasan")
my_function_2()
my_function_2("Alisa")


print("***")


# Keyword Arguments

# You can send arguments with the key = value syntax.
def my_function_3(animal,name):
    print("I have a" + " " + animal)
    print(f"My {animal}'s name is {name}")

my_function_3(name="Bubu",animal="Cat")


print("***")


# Positional Arguments

# When you call a function with arguments without using keywords, they are called positional arguments.
# Positional arguments must be in the correct order:
def my_function_4(animal,name):
    print(f"I have a {animal}")
    print(f"My {animal}'s name is {name}")
my_function_4("Dog", "Bubu")


print("***")


# Passing Different Data Types

# You can send any data type as an argument to a function (string, number, list, dictionary, etc.).
# The data type will be preserved inside the function:
def my_function_5(fruits):
    for x in fruits:
        print(x)
my_fruits = ["apple","banana","cherry"]
# my_function_5(["apple","banana","cherry"])
my_function_5(my_fruits)


print("***")


# Return Values

# Functions can return values using the return statement:
def my_function_6(x,y):
    return x + y 
result = my_function_6(5,1) 
# print(my_function_6(2,2))
print(result)


print("***")


# Positional-Only Arguments

# You can specify that a function can have ONLY positional arguments.
# To specify positional-only arguments, add , / after the arguments:
def my_function_7(name, /):
    print(f"Hello {name}")
my_function_7("Pukki")


print("***")


# Keyword-Only Arguments

# To specify that a function can have only keyword arguments, add *, before the arguments:
def my_function_8(*, name):
    print(f"Hello {name}")
my_function_8( name= "Tonni")


print("***")


# Combining Positional-Only and Keyword-Only

# You can combine both argument types in the same function.
# Arguments before / are positional-only, and arguments after * are keyword-only:
def my_function_9(a,b, /,c, *,d,):
    return a + b + c + d 
print(my_function_9(5,5,4,d = 4))