# List Comprehension


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = []

for x in fruits:
    if "a" in x :
        new_list.append(x)

print(new_list)

# With list comprehension you can do all that with only one line of code:
new_list_1 = [x for x in fruits if "a" in x]
print(new_list_1)


# Condition

new_list_2 = [x for x in fruits if x != "apple"]
print(new_list_2)

# Iterable

# The iterable can be any iterable object, like a list, tuple, set etc.

new_list_3 = [ x ** 2   for x in range(10) ]
print(new_list_3)