# Loop in Dictionaries

# Loop Through a Dictionary

# You can loop through a dictionary by using a for loop.
# When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.
this_dict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in this_dict:
    print(x) # ekhon sudu key asbe

print("***")

for x in this_dict:
    print(this_dict[x]) # ekhon values asbe

print("***")

for x in this_dict.values():
    print(x)

print("***")

for x , y  in this_dict.items():
    print(x,y)