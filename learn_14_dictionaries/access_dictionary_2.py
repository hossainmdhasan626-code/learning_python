# Python - Access dictionary




# Accessing Items

# You can access the items of a dictionary by referring to its key name, inside square brackets:

this_dic = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = this_dic["model"]
# There is also a method called get() that will give you the same result:
y = this_dic.get("brand")
print(x)
print(y)

print("***")

# Get Keys

# The keys() method will return a list of all the keys in the dictionary.
this_dic_1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x_1 = this_dic.keys()
print(x_1)


# Get Values

# The values() method will return a list of all the values in the dictionary.
this_dic_2 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(this_dic_2.values())


# Get Items

# The items() method will return each item in a dictionary, as tuples in a list.
this_dic_3 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(this_dic_3.items())


# Check if Key Exists

# To determine if a specified key is present in a dictionary use the in keyword:
this_dic_3 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in this_dic_3 : 
    print("Yes, 'model' is one of the keys is the this_dic_3 dictionary")