# Remove Set 


# Remove Item

# To remove an item in a set, use the remove(), or the discard() method.

this_set = {"apple", "banana", "cherry"}
this_set.remove("banana")
# Note: If the item to remove does not exist, remove() will raise an error.
print(this_set)


this_set.discard("apple")
# Note: If the item to remove does not exist, discard() will NOT raise an error.
print(this_set)


# You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.
# The return value of the pop() method is the removed item.
this_set_1 = {"apple", "banana", "cherry"}
# Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.
x = this_set_1.pop()
print(x)
print(this_set_1)


# The del keyword will delete the set completely:
this_set_2 = {"apple", "banana", "cherry"}
del this_set_2
# print(this_set_2) # This will be a Error