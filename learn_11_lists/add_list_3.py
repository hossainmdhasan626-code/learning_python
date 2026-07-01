# Add List 

name = ["Hasan","Maisha","Tanha","Rafi","Siam","Kona"]

# Append Items

# To add an item to the end of the list, use the append() method:
name.append("Maria")


# Insert Items

# To insert a list item at a specified index, use the insert() method.
# The insert() method inserts an item at the specified index:

name.insert(0,"Mahmud")


# Extend List

# To append elements from another list to the current list, use the extend() method.

name2 = ["Siki-gami","Nakamura"]

name.extend(name2)


# Add Any Iterable

# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

name3 = ["Suvashini", "Sukeshini"]

name.extend(name3)


print(name)