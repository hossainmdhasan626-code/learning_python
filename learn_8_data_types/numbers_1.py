# Numbers

import random

x = 1    # int
y = 2.8  # float
z = 1j   # complex
# There are three numeric types in Python:

print(type(x))
print(type(y))
print(type(z))
# To verify the type of any object in Python, use the type() function:


# Int

# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

x1 = 1
y1 = 35656222554887711
z1 = -3255522

print(type(x1))
print(type(y1))
print(type(z1))


# Float

# Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

x2 = 1.10
y2 = 1.0
z2 = -35.59

print(type(x2))
print(type(y2))
print(type(z2))


x3 = 35e3    # এর মানে হলো: 35 * 10^3 (অর্থাৎ 35 * 1000)
print(x3)    # আউটপুট আসবে: 35000.0 (দেখুন, এটি কিন্তু float)

y3 = 12E4    # এর মানে হলো: 12 * 10^4
print(y3)    # আউটপুট আসবে: 120000.0
# হ্যাঁ, একদম ঠিক! এটি পাইথনে (এবং অন্যান্য অনেক প্রোগ্রামিং ল্যাঙ্গুয়েজে) বড় বড় সংখ্যা বা খুব ছোট দশমিক সংখ্যা সহজে লেখার একটি বৈজ্ঞানিক পদ্ধতি। 
# একে বলা হয় Scientific Notation বা Exponential Notation।এখানে e বা E (ছোট বা বড় হাতের যেকোনোটি হতে পারে) মানে হলো 
# "১০ এর পাওয়ার" (Power of 10) বা $10^x$।চলুন খুব সহজে জিনিসটা ভেঙে বুঝি:১. পজিটিভ পাওয়ার (বড় সংখ্যার জন্য)যখন আপনি e-এর পরে একটি পজিটিভ সংখ্যা লিখবেন, 
# তার মানে হলো বামপাশের সংখ্যার সাথে ১০-এর পাওয়ার গুণ হচ্ছে। সহজ কথায়—দশমিক বিন্দুটি ডানদিকে তত ঘর সরে যাবে (বা ততগুলো শূন্য বসবে)।


# Complex

# Complex numbers are written with a "j" as the imaginary part:

x4 = 3+5j
y4 = 5j
z4 = -5j

print(type(x4))
print(type(y4))
print(type(z4))

x5 = 3 + 4j
y5 = 5J       # বড় হাতের J-ও চলবে
z5 = 2 + 1j   # ১ থাকলেও 1j লিখতে হবে

print(type(x5))
print(type(y5))
print(type(z5))


# Type Conversion

# You can convert from one type to another with the int(), float(), and complex() methods:
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
# Note: You cannot convert complex numbers into another number type.

# Random Number

# Python does not have a random() function to make a random number, 
# but Python has a built-in module called random that can be used to make random numbers:
print(random.randrange(1,1000))