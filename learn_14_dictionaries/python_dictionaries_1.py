# Python Dictionaries

this_dic = {
    "brand":"Ford",
    "model":"Mustang",
    "year": 1964
}


# Dictionary

# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# Dictionaries are written with curly brackets, and have keys and values:
this_dic = {
    "brand":"Ford",
    "model":"Mustang",
    "year": 1964
}
print(this_dic)


# Duplicates Not Allowed

# Dictionaries cannot have two items with the same key:

this_dic_1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(this_dic_1) # jekono ekta year kew bad jabe


# Dictionary Length

# To determine how many items a dictionary has, use the len() function:
this_dic_2 = {
    "brand":"Ford",
    "model":"Mustang",
    "year": 1964
}
print(len(this_dic_2))


# Dictionary Items - Data Types

# The values in dictionary items can be of any data type:
this_dic_3 = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}


# type()

# From Python's perspective, dictionaries are defined as objects with the data type 'dict':
this_dic_4 = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(type(this_dic_4))


# The dict() Constructor

# It is also possible to use the dict() constructor to make a dictionary.
this_dic_5 = dict(name = "John", age = 36, country = "Norway")
print(this_dic_5)
