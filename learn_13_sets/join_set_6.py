# Join set 




# Join Sets


# Union # *** Note: Both union() and update() will exclude any duplicate items.


# The union() method returns a new set with all items from both sets.
set_1 = {"a", "b", "c"}
set_2 = {1, 2, 3}
set_3 = set_1.union(set_2)
print(set_3)


# You can use the | operator instead of the union() method, and you will get the same result.
set_4 = {"a", "b", "c"}
set_5 = {1,2,3}
set_6 = set_4 | set_5
print(set_6)

print("***")
# Join Multiple Sets

# All the joining methods and operators can be used to join multiple sets.
# When using a method, just add more sets in the parentheses, separated by commas:
set_7 = {"a", "b", "c"}
set_8 = {1, 2, 3}
set_9 = {"John", "Elena"}
set_10 = {"apple", "bananas", "cherry"}
set_11 = set_7.union(set_8,set_9,set_10) 
# set_11 = set_7 | set_8 | set_9 | set_10 # Eta o kaj kore
print(set_11)


# Join a Set and a Tuple

# The union() method allows you to join a set with other data types, like lists or tuples.
# The result will be a set.
set_12 = {"a", "b", "c"}
set_13 = (1, 2, 3)
set_14 = set_12.union(set_13) # Note: The  | operator only allows you to join sets with sets, and not with other data types like you can with the  union() method.
print(set_14)


# Update

# The update() method inserts all items from one set into another.
# The update() changes the original set, and does not return a new set.
set_15 = {"a", "b", "c"}
set_16 = {1, 2, 3}
set_15.update(set_16) # Note: Both union() and update() will exclude any duplicate items.
print(set_15)


# Intersection

# Keep ONLY the duplicates
# The intersection() method will return a new set, that only contains the items that are present in both sets.

set_17 = {"apple", "banana", "cherry"}
set_18 = {"google", "microsoft", "apple"}
set_19 = set_17.intersection(set_18)
print(set_19)

# You can use the & operator instead of the intersection() method, and you will get the same result.

set_20 = {"apple", "banana", "cherry"}
set_21 = {"google", "microsoft", "apple"}
set_22 = set_20 & set_21 # Note: The & operator only allows you to join sets with sets, and not with other data types like you can with the intersection() method.
print(set_22)


# The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
set_23 = {"apple", "banana", "cherry"}
set_24 = {"google", "microsoft", "apple"}
set_23.intersection_update(set_24)
print(set_23)


# Difference

# The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
set_25 = {"apple", "banana", "cherry"}
set_26 = {"google", "microsoft", "apple"}
set_27 = set_25.difference(set_26)
print(set_27)


# You can use the - operator instead of the difference() method, and you will get the same result.


set_28 = {"apple", "banana", "cherry"}
set_29 = {"google", "microsoft", "apple"}
set_30 = set_28 - set_29   # Note: The - operator only allows you to join sets with sets, and not with other data types like you can with the difference() method.
print(set_30)


# The difference_update() method will keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.
set_31 = {"apple", "banana", "cherry"}
set_32 = {"google", "microsoft", "apple"}
set_31.difference_update(set_32)
print(set_31)


# Symmetric Differences

# The symmetric_difference() method will keep only the elements that are NOT present in both sets.
set_33 = {"apple", "banana", "cherry"}
set_34 = {"google", "microsoft", "apple"}
set_35 = set_33.symmetric_difference(set_34)
print(set_35)


# You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.
set_36 = {"apple", "banana", "cherry"}
set_37 = {"google", "microsoft", "apple"}
set_38 = set_36 ^ set_37 # Note: The ^ operator only allows you to join sets with sets, and not with other data types like you can with the symmetric_difference() method.
print(set_38)


# Note: The ^ operator only allows you to join sets with sets, and not with other data types like you can with the symmetric_difference() method.


# The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set.
set_39 = {"apple", "banana", "cherry"}
set_40 = {"google", "microsoft", "apple"}
set_39.symmetric_difference_update(set_40)
print(set_39)
