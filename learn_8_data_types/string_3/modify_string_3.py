# Modify String 

# Upper Case 

# The upper() method returns the string in upper case:

a = "Hello, World!"
print(a.upper())


# Lower Case

# The lower() method returns the string in lower case:

print(a.lower())


# Strip()

# The strip() function in Python removes all blank spaces or gaps from both the beginning and end of a string.

a1 = "   Hellow Hasan   "
print(a1.strip())
# strip() never touches the spaces between the text. For example:


text = "   Hasan   "
# lstrip() (Left Strip): This only removes the left or leading space. The right space remains as is.
# rstrip() (Right Strip): This only removes the right or trailing spaces. The left spaces remain as they are.
print(text.lstrip()) # আউটপুট: "Hasan   " (শুধু শুরুর স্পেস গেছে)
print(text.rstrip()) # আউটপুট: "   Hasan" (শুধু শেষের স্পেস গেছে)


# replace() 

# The replace() method replaces a string with another string:

a2 = "Hello, alisa How are you today ?"
print(a2.replace("H","j"))


# Split String

text = "apple, banana mango"
result = text.split()

print(result)
# আউটপুট আসবে: ['apple,', 'banana', 'mango']

text = "apple, banana mango"
result = text.split(",") # পাইথনকে বলে দিলাম: কমা দেখলেই কাটো!
# এবার ম্যাজিক দেখুন: এবার কিন্তু কমার জায়গায় ভেঙে দুটি আলাদা ভ্যালু হয়ে গেছে! প্রথম ভ্যালু apple এবং দ্বিতীয় ভ্যালু  banana mango (কারণ এদের মাঝে কোনো কমা ছিল না, শুধু স্পেস ছিল)।
print(result)
# আউটপুট আসবে: ['apple', ' banana mango']