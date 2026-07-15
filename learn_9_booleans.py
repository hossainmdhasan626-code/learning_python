# Python Booleans

# When you compare two values, the expression is evaluated and Python returns the Boolean answer:

print(10 > 9)
print(10 == 9)
print(10 < 9)


# When you run a condition in an if statement, Python returns True or False:

a = 200
b = 33

if b > a :
    print("b is greater than a")
else : 
    print("b is not greater than a")


# পাইথনে bool() ফাংশনটি শুধুমাত্র তখনই False দেয় যখন তার ভেতরে সম্পূর্ণ খালি বা শূন্য কিছু থাকে। যেমন: খালি স্ট্রিং "", শূন্য 0, খালি লিস্ট [], বা None।
# কিন্তু আপনি যখন bool("False") লিখেছেন, তখন পাইথনের কাছে ওটা "False" শব্দ নয়, ওটা হলো একটা ভর্তি স্ট্রিং (যার ভেতর ৫টি অক্ষর আছে)। যেহেতু স্ট্রিংটি খালি নয়, তাই পাইথন একে True হিসেবে গণ্য করেছে!

