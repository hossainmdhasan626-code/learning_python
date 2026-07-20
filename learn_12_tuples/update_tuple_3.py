# Update Tuple

# Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.
# But there are some workarounds.


# Change Tuple Values

# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
x = ("apple","banana","kiwi")
print(x)
y = list(x)
print(y)
y.append("orange")
print(y)
x = tuple(y)
print(x)


# You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:
this_tuple = ("apple","banana","cherry")
y = ("orange","pukki","chukki","mukki")
this_tuple += y
print(this_tuple)


# Remove Items

# Note: You cannot remove items in a tuple.
# Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items:
this_tuple_1 = ("apple","banana","cherry")
print(this_tuple_1)
y = list(this_tuple_1)
print(y)
y.remove("banana")
print(y)
this_tuple_1 = tuple(y)
print(this_tuple_1)

# You can delete the tuple completely:
# The del keyword can delete the tuple completely:
this_tuple_2 = ("apple","banana","cherry")
del this_tuple_2
# print(this_tuple_2) #this will raise an error because the tuple no longer exists