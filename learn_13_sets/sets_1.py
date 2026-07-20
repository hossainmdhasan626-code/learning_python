# Python Sets

myset = {"apple", "banana", "cherry"}

# Set

# Sets are used to store multiple items in a single variable.
# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
# A set is a collection which is unordered, unchangeable*, and unindexed.

# Sets are written with curly brackets.
this_set = {"apple","banana","cherry"}
print(this_set)
# আপনি প্রিন্ট করার সময় কোনো ম্যানিপুলেশন করছেন না ঠিকই, কিন্তু পাইথন প্রতিবার নতুন করে রান হওয়ার সময় ব্যাকগ্রাউন্ডে মেমোরির ঘর নম্বরগুলো লটারির মতো উলটপালট করে দেয়। 
# আর সেট যেহেতু মেমোরির ঘর নম্বর অনুযায়ী ছোট থেকে বড় সিরিয়ালে প্রিন্ট করে, তাই আমাদের চোখে প্রতিবার এর অর্ডার বা সাজানোটা আলাদা লাগে।


# Duplicates Not Allowed

# Sets cannot have two items with the same value.
this_set_1 = {"apple","banana","cherry","apple"}
print(this_set_1)


# পাইথনের একটি গভীর ইন্টারনাল লজিক বোঝানো হচ্ছে। সহজ ভাষায় এর মানে হলো: পাইথনের সেটের (Set) ভেতরে True এবং সংখ্যা 1 কে হুবহু একই জিনিস বা 
# ডুপ্লিকেট (Duplicate) হিসেবে গণ্য করা হয়। যেহেতু সেটের প্রধান নিয়মই হলো সে কোনো ডুপ্লিকেট জিনিস ভেতরে রাখে না, তাই আপনি যদি কোনো সেটের ভেতর True এবং 
# 1 দুটিই একসাথে ঢোকাতে যান, সেট তাদের মধ্যে থেকে যেকোনো একটাকে রাখবে আর অন্যটাকে ডুপ্লিকেট মনে করে ফেলে দেবে!

# আমরা সেটের ভেতর ১ এবং True দুটিই দিচ্ছি
this_set_2 = {1, "apple", True, "banana"}

print(this_set_2) 
# আউটপুট আসতে পারে: {1, 'apple', 'banana'} 
# খেয়াল করুন, True কিন্তু গায়েব হয়ে গেছে!

# আবার আপনি যদি True কে আগে লেখেন, তবে 1 গায়েব হয়ে যাবে:

this_set_3 = {True, "apple", 1, "banana"}

print(this_set_3) 
# আউটপুট আসবে: {True, 'apple', 'banana'}
# এবার সংখ্যা ১ গায়েব হয়ে গেছে!

# *** একইভাবে False এবং সংখ্যা 0-কেও সেটের ভেতর হুবহু এক বা ডুপ্লিকেট ধরা হয়!


# Get the Length of a Set

# To determine how many items a set has, use the len() function.

this_set_4 = {"apple","banana","cherry"}
print(len(this_set_4))


# Set Items - Data Types

# Set items can be of any data type:

this_set_5_1 = {"apple", "banana", "cherry"}
this_set_5_2 = {1, 5, 7, 9, 3}
this_set_5_3 = {True, False, False}
this_set_5_4 = {"abc", 34, True, 40, "male"}


# type()

my_set_type = {"apple", "banana", "cherry"}
print(type(my_set_type))


# The set() Constructor

# It is also possible to use the set() constructor to make a set.
this_set_6_1 = ["Hasan","Maisha","Tanha","Rafi","Siam","Kona"]
this_set_6_2 = set(this_set_6_1)
this_set_6_3 = set(("apple", "banana", "cherry")) # note the double round-brackets

print(this_set_6_2)
print(this_set_6_3)