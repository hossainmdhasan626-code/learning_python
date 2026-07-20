# Python - range 


# The built-in range() function returns an immutable sequence of numbers, commonly used for looping a specific number of times.
# Note: Immutable means that it cannot be modified after it is created.

# Creating ranges

# The range() function can be called with 1, 2, or 3 arguments, using this syntax:

# Call range() With One Argument

# If the range function is called with only one argument, the argument represents the stop value.
# The start argument is optional, and if not provided, it defaults to 0.
# range(10) returns a sequence of each number from 0 to 9. (The start argument, 0 is inclusive, and the stop argument, 10 is exclusive).
x = range(11)
print(x)
print(list(x))


print("***")


# Call range() With Two Arguments

# If the range function is called with two arguments, the first argument represents the start value, and the second argument represents the stop value.
x_1 = range(3,11)
print(list(x_1))


print("***")


# Call range() With Three Arguments

# If the range function is called with three arguments, the third argument represents the step value.
# The step value means the difference between each number in the sequence. It is optional, and if not provided, it defaults to 1.
x_3 = range(2,11,2)
print(list(x_3))


print("***")


# Using ranges

# Ranges are often used in for loops to iterate over a sequence of numbers.
for i in range(11):
    print(i)


print("***")


# Slicing Ranges

# Like other sequences, ranges can be sliced to extract a subsequence.
r = list(range(11))
print(r[:5])
print(r[5:])


print("***")


# Membership Testing 

# Ranges support membership testing with the in operator.
x_4 = range(11)
print(6 in x_4)
print(11 in x_4)


print("***")


# Length

# Ranges support the len() function to get the number of elements in the range.
x_5 = range(11)
print(len(r))