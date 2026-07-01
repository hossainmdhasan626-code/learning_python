# Python - Change Dictionary Items




# Change Values

# You can change the value of a specific item by referring to its key name:
this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
this_dict["year"] = 2018
print(this_dict)


# Update Dictionary

# The update() method will update the dictionary with the items from the given argument.
# The argument must be a dictionary, or an iterable object with key:value pairs.
this_dict_1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
this_dict_1.update({"brand":"ffff"})
print(this_dict_1)