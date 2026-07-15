# Python Inheritance

# Python Inheritance

# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.


# Create a Parent Class

# Any class can be a parent class, so the syntax is the same as creating any other class:

class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def print_name(self):
        print(self.fname,self.lname)

p_1 = Person("Md" ,"Hasan")
p_1.print_name()

# Create a Child Class
# To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:

class Student(Person):
    pass

p_2 = Student("Md","Mudra000")
p_2.print_name()


print("***")


# parent 1
class Car:
    def drive(self):
        print("🚗 মাটির ওপর গাড়ি চলছে... ব্রুম ব্রুম!")


# parent 2 
class Airplane:
    def fly(self):
        print("✈️ আকাশে বিমান উড়ছে... শুউউউ!")

# child 
class FlyingCar(Car,Airplane):
    def special_feature(self):
        print("🤖 আমি একই সাথে চলতে এবং উড়তে পারি!")


my_vehicle = FlyingCar()

my_vehicle.drive()
my_vehicle.fly()
my_vehicle.special_feature()


print("***")


# Use the super() Function

# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:
class Father:
    def __init__(self):
        self.money = 50000  # 💵 প্যারেন্টের প্রোপার্টি

    def drive_car(self):   # 🚗 প্যারেন্টের সাধারণ মেথড
        print("বাবা গাড়ি চালাতে পারেন।")

# চাইল্ড ক্লাস নিজের একটি __init__ ব্যবহার করছে
class Son(Father):
    def __init__(self):
        super().__init__()
        self.pocket_money = 500  # চাইল্ডের নিজস্ব প্রপার্টি

# অবজেক্ট বানাচ্ছি
boy = Son()

# ১. সাধারণ মেথড ইনহেরিটেন্স টেস্ট (এটি ১০০% কাজ করবে!)
boy.drive_car()  # আউটপুট: বাবা গাড়ি চালাতে পারেন। (ক্ষমতা হারায়নি!)

# ২. প্রোপার্টি ইনহেরিটেন্স টেস্ট (🚨 এখানেই এরর আসবে!)
print(boy.money)  # AttributeError: 'Son' object has no attribute 'money'