# Python - copy Dictionary

# Copy a Dictionary

# You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
# There are ways to make a copy, one way is to use the built-in Dictionary method copy().
this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
this_dict_copy = this_dict.copy()
print(this_dict is this_dict_copy )


# Another way to make a copy is to use the built-in function dict().
this_dict_1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
this_dict_2 = dict(this_dict_1)
print(this_dict_2)
print(this_dict_1 is this_dict_2)