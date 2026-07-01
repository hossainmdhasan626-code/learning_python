# Access set  

# You cannot access items in a set by referring to an index or a key.
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

this_set = {"apple","banana","kiwi"}
 
for i in this_set:
        print(i)
    
print("banana" not in this_set)