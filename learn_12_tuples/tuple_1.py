# Tuple




# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.

this_tuple = ("apple","banana","cherry")
print(type(this_tuple))
print(this_tuple)



# Tuple Items


# Tuple items are ordered, unchangeable, and allow duplicate values.
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

# Ordered
# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

# Unchangeable
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

# Tuple Length
# To determine how many items a tuple has, use the len() function:
this_tuple_1 = ("apple","banana","cherry")
print(this_tuple_1)

# Create Tuple With One Item
# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

this_tuple_2 = ("apple",)
print(this_tuple_2)

this_tuple_3 = ("apple") # Not a tuple
print(this_tuple_3)

# Tuple Items - Data Types
this_tuple_4_1 = ("apple","banana","cherry")
this_tuple_4_2 = (1,2,3)
this_tuple_4_3 = (True,False,True)

# A tuple can contain different data types:
# A tuple with strings, integers and boolean values:
this_tuple_5 = ("apple", 34 , True , 40 , "male")

# The tuple() Constructor
# It is also possible to use the tuple() constructor to make a tuple.
this_tuple_6 = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(this_tuple_6)