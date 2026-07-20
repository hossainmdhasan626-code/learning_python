import first_module
import secend_module as sec_mod
import platform
from third_module import person_1

# Python - Modules 


# What is a Module?

# Consider a module to be the same as a code library.
# A file containing a set of functions you want to include in your application.

first_module.my_module(fname= "Md Mahmudul") 
# Note: When using a function from a module, use the syntax: module_name.function_name.


print("***")


# Variables in Module

# The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc):

print(first_module.person_1["age"])


print("***")


# Naming a Module

# You can name the module file whatever you like, but it must have the file extension .py
# Re-naming a Module
# You can create an alias when you import a module, by using the as keyword:

print(sec_mod.person_1["name"])


print("***")


# Built-in Modules

# There are several built-in modules in Python, which you can import whenever you like.

print(platform.system()) 


print("***")


# Using the dir() Function

# There is a built-in function to list all the function names (or variable names) in a module. The dir() function:
# print(dir(platform))


print("***")


# Import From Module

# You can choose to import only parts from a module, by using the from keyword.
print(person_1["country"])
# Note: When importing using the from keyword, do not use the module name when referring to elements in the module. Example: person1["age"], not mymodule.person1["age"]


print("***")


