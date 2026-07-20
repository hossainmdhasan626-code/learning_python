# Python For Loop


# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# The for loop does not require an indexing variable to set beforehand.


print("***")


# Looping Through a String

# Even strings are iterable objects, they contain a sequence of characters:
for x  in "Hasan":
    print(x)


print("***")


# The break Statement

# With the break statement we can stop the loop before it has looped through all the items:
fruits_1 = ["apple", "banana", "cherry"]
for x in fruits_1:
    print(x)
    if x == "banana":
        break


print("***")



# The continue Statement

# With the continue statement we can stop the current iteration of the loop, and continue with the next:
fruits_2 = ["apple", "banana", "cherry"]
for x in fruits_2:
    if x == "banana":
        continue
    print(x)


print("***")


# The range() Function

# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
for x in range(6): # *** Note that range(6) is not the values of 0 to 6, but the values 0 to 5.
    print(x)


print("***")


# The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):
for x in range(2,6):
    print(x)


print("***")


# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
for x in range(2,30,3):
    print(x)


print("***")


# Else in For Loop

# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
for x in range(6):
    print(x)
else:
    print("Finally finished")

# Note: The else block will NOT be executed if the loop is stopped by a break statement.

