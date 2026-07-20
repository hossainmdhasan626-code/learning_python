# Loop in tuple


# Loop Through a Tuple

# You can loop through the tuple items by using a for loop.
thistuple = ("apple", "banana", "cherry")
for x in thistuple :
    print(x)

print("***")

thistuple_1 = ("apple", "banana", "cherry")

for x in range(len(thistuple)):
    print(thistuple_1[x])

print("***")

# Using a While Loop

thistuple_2 = ("apple", "banana", "cherry")

i = 0 
while i < len(thistuple_2):
    print(thistuple_2[i])
    i += 1
