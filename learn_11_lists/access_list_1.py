# Access Items

# List items are indexed and you can access them by referring to the index number:

name = ["Hasan","Maisha","Tanha","Rafi","Siam","Kona"]

print(name[1]) # Note: The first item has index 0.


# Negative Indexing

# Negative indexing means start from the end

# -1 refers to the last item, -2 refers to the second last item etc.

print(name[-1])


# Range of Indexes

# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new list with the specified items.

print(name[2:4]) # Note: The search will start at index 2 (included) and end at index 4 (not included).


# By leaving out the start value, the range will start at the first item:
print(name[:5])


# By leaving out the end value, the range will go on to the end of the list:
print(name[2:])


# Range of Negative Indexes

# Specify negative indexes if you want to start the search from the end of the list:
# This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):
print(name[-4:-1])

#  By leaving out the end value, the range will go on to the end of the list:
print(name[-4:])

# By leaving out the start value, the range will start at the first item:
print(name[:-2])


# Check if Item Exists

# To determine if a specified item is present in a list use the in keyword:

index_of_rafi = name.index("Rafi")

if "Rafi" in name :
    print("Yes, Rafi is in the name list")
else:
    print("Rafi was't in the name list")