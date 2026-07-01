# Python - Remove Dictionary Items 

# Removing Items


# The pop() method removes the item with the specified key name:

this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
this_dict.pop("model")
print(this_dict)


# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
this_dict_1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
this_dict_1.popitem()
print(this_dict_1)


# The del keyword removes the item with the specified key name:
this_dict_2 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del this_dict_2 # If i print it now it will be a error .

print("***")

# The clear() method empties the dictionary:
this_dict_3 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
this_dict_3.clear()
print(this_dict_3)
