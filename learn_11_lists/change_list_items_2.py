# Change List Items

name = ["Hasan","Maisha","Tanha","Rafi","Siam","Kona"]


# To change the value of a specific item, refer to the index number:
name[0] = "Mahmudul Hasan"


# Change a Range of Item Values

# To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:
name[1:3] = ["Mim","Tanju"]

print(len(name))


# If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:

name[1:3] = ["Maisha","Tanha","Alisha"]

print(len(name)) # Note: The length of the list will change when the number of items inserted does not match the number of items replaced.


# Insert Items

# To insert a new list item, without replacing any of the existing values, we can use the insert() method.
# The insert() method inserts an item at the specified index:
name.insert(0,"Hasan")



print(name)
