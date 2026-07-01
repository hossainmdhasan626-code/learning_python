# Remove List 


name = ["Hasan","Maisha","Tanha","Rafi","Hasan","Siam","Kona"]


# Remove Specified Item

# The remove() method removes the specified item.
# If there are more than one item with the specified value, the remove() method removes the first occurrence:

name.remove("Hasan")


# Remove Specified Index

# The pop() method removes the specified index.

name.pop(3) # If you do not specify the index, the pop() method removes the last item.


# The del keyword also removes the specified index:

del name[0] 

# The del keyword can also delete the list completely.this will cause an error because you have succsesfully deleted list.


# Clear the List

# The clear() method empties the list.
# The list still remains, but it has no content.

name.clear()

print(name)