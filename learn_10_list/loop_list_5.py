# Loop List 


name = ["Hasan","Maisha","Tanha","Rafi","Siam","Kona"]


# Loop Through a List

# You can loop through the list items by using a for loop:

for n in name :
    print(n)


# Loop Through the Index Numbers


# You can also loop through the list items by referring to their index number.
# Use the range() and len() functions to create a suitable iterable.

for n in range(len(name)) : 
    print(name[n])


# Using a While Loop

# Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.
# Remember to increase the index by 1 after each iteration.

i = 0 

while i < len(name) :
    print(name[i])
    i += 1
