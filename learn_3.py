# Indentation : শুধুমাত্র কোডের লাইনের শুরুর স্পেস (Space) বা খালি জায়গাকেই "Indentation" বলে।
if 5 > 2:
    print("Five is greater then two") 

# Eta te indentation na thay error dibe
# if 5 > 2:
# print("Five is greater then two")   

# Ekta if ba ekstha thaka sokol commend er indentation same na hole error dibee .
if 5 > 2:
    print("Five is greater then two")   
    # Ekhane uporer ar nicer print() er indentation same tai eta thik ache .
    print("Five is greater then two")

    # if 5 > 2:
    #     print("Five is greater then two")   
    #     # Ekhane uporer ar nicer print() er indentation same na tai eta error dibe .
    #      print("Five is greater then two")

# পাইথনের একটি অফিশিয়াল গাইডলাইন বা নিয়মকানুন আছে, যার নাম PEP 8 (Python Enhancement Proposal 8)। এটি হলো পাইথন ডেভেলপারদের জন্য একটি "স্টাইল গাইড" বা ভদ্রতা।

# সেখানে বলা হয়েছে:

# বিশ্বজুড়ে সমস্ত পাইথন প্রোগ্রামাররা যেন একে অপরের কোড সহজে বুঝতে পারে, সেজন্য স্ট্যান্ডার্ড হিসেবে ৪টি স্পেস দেওয়া উচিত।

# এটি কোডকে দেখতে সবচেয়ে বেশি সুন্দর ও প্রফেশনাল বানায়।

# আপনি ২টি স্পেস দিয়ে কোড শুরু করলে পুরো ব্লকে ২টি করেই দিতে হবে, ৪টি দিয়ে শুরু করলে ৪টিই দিতে হবে। তবে প্রফেশনাল কোডিং দুনিয়ায় সবাই ৪টি স্পেস বা ১টি Tab ব্যবহার করে। (VS Code-এ Tab চাপলে সেটি অটোমেটিক ৪টি স্পেসেই রূপান্তর হয়ে যায়)।