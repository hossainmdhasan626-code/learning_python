# Add set items 


# Add Items

# To add one item to a set use the add() method.
this_set = {"apple", "banana", "cherry"}
this_set.add("orange")
print(this_set)


# Add Sets

# To add items from another set into the current set, use the update() method.

this_set_1_1 = {"apple", "banana", "cherry"}
this_set_1_2 = {"pineapple", "mango", "papaya"}
this_set_1_1.update(this_set_1_2)
print(this_set_1_1)


# Add Any Iterable

# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

thisset_2_1 = {"apple", "banana", "cherry"}
mylist_2_2 = ["kiwi", "orange"]

thisset_2_1.update(mylist_2_2)

print(thisset_2_1)