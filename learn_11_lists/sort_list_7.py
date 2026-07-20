# Short List 


# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
short_list = ["orange", "mango", "kiwi", "pineapple", "banana"]
short_list.sort()
print(short_list)

short_list_1 = [100, 50, 65, 82, 23,1,0]
short_list_1.sort() # reverse= True
print(short_list_1)


# Sort Descending

# To sort descending, use the keyword argument reverse = True:

short_list.sort(reverse= True)
print(short_list)


# Customize Sort Function

# You can also customize your own function by using the keyword argument key = function.
# The function will return a number that will be used to sort the list (the lowest number first):
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)


# Case Insensitive Sort

# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
thislist_1 = ["banana", "Orange", "Kiwi", "cherry"]
thislist_1.sort()
print(thislist_1)


# Luckily we can use built-in functions as key functions when sorting a list.
# So if you want a case-insensitive sort function, use str.lower as a key function:

thislist_2 = ["banana", "Orange", "Kiwi", "cherry"]
thislist_2.sort(key = str.lower)
print(thislist_2)


# Reverse Order

# What if you want to reverse the order of a list, regardless of the alphabet?
# The reverse() method reverses the current sorting order of the elements.

thislist_3 = ["banana", "Orange", "Kiwi", "cherry"]
thislist_3.reverse()
print(thislist_3)