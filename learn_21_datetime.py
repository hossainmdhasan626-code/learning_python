import datetime 

# Python - Datetime


# Python Dates

# A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.

x = datetime.datetime.now()
print(x.strftime("%B")) # strftime full form "String Format Time"


print("***")


# Creating Date Objects

# To create a date, we can use the datetime() class (constructor) of the datetime module.

# The datetime() class requires three parameters to create a date: year, month, day.
my_birthday = datetime.datetime(2006,12,17) # Kono karono kono nirdisto date er details ber korte hole 
print(my_birthday.strftime("%A"))


