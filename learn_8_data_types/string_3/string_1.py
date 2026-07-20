# Python String

# Strings
# Strings in python are surrounded by either single quotation marks, or double quotation marks.
# 'hello' is the same as "hello".
# You can display a string literal with the print() function:

print("hello")
print('hello')


# Quotes Inside Quotes

# You can use quotes inside a string, as long as they don't match the quotes surrounding the string:

print("It's alright")
print("He is called 'johnny'")


# Assign String to a Variable

# Assigning a string to a variable is done with the variable name followed by an equal sign and the string:

a = "Hello"
print(a)


# Multiline Strings

# You can assign a multiline string to a variable by using three quotes: Or three single quotes:

print("""Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.""")


# Strings are Arrays

# Like many other popular programming languages, strings in Python are arrays of unicode characters.
# However, Python does not have a character data type, a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string.

a1 = "Hello, World!"
print(a1[1])


# Looping Through a String

# Since strings are arrays, we can loop through the characters in a string, with a for loop.

for x in "banana":
  print(x)


# String Length

# To get the length of a string, use the len() function.

a2 = "Hello,   World!"
print(len(a2))


# Check String in

# To check if a certain phrase or character is present in a string, we can use the keyword in.

text = "Govir rater shoroni, chuteche norog nogori"
user = {"name":"Hasan","age":20}

print("nogori" in text)
print("name" in user)

# Use it in an if statement:

text1 = "The best things in life are free"
if " " in text1 :
  print("pukki")


# Check if NOT

# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.

text2 = "Hello tanha . How are you ?"
print("Hasan" not in text2)

# Use it in an if statement:

if "mim" not in text2:
  print("mim was't in text2")

