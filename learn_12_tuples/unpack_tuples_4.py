# Unpack Tuples

# In Python, we are also allowed to extract the values back into variables. This is called "unpacking":
fruits = ("apple", "banana", "cherry")
(green,yellow,red) = fruits
# Note: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.
print(green)
print(yellow)
print(red)


# Using Asterisk*

print("***")
# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:
fruits_1 = ("apple", "banana", "cherry","strawberry", "raspberry")
(green_1,yellow_1,*red_1) =  fruits_1

print(green_1)
print(yellow_1)
print(red_1)

print("***")

fruits_2 = ("apple", "banana", "cherry","strawberry", "raspberry")
(green_2,*yellow_2,red_2) =  fruits_2

print(green_2)
print(yellow_2)
print(red_2)

print("***")

fruits_3 = ("apple", "banana", "cherry","strawberry", "raspberry")
(*green_3,yellow_3,red_3) =  fruits_3

print(green_3)
print(yellow_3)
print(red_3)

print("***")



