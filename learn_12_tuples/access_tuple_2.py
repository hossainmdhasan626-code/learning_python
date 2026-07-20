# Access Tuple 


# You can access tuple items by referring to the index number, inside square brackets:

this_tuple = ("apple","banana","cherry","orange", "kiwi", "melon", "mango")
print(this_tuple[1])
print(this_tuple[1:5])
print(this_tuple[2:])
print(this_tuple[:4])


# Negative Indexing

print("Negative Indexing")

# Negative indexing means start from the end.
# -1 refers to the last item, -2 refers to the second last item etc.
this_tuple_1 = ("apple","banana","cherry","orange", "kiwi", "melon", "mango")
print(this_tuple_1[-1])
print(this_tuple_1[-4:-1])
print(this_tuple_1[-5:])
print(this_tuple_1[:-3])