# Python Logical Operators


# The and Operator

# The and keyword is a logical operator, and is used to combine conditional statements. Both conditions must be true for the entire expression to be true.
a = 200
b = 33 
c = 500
if a > b and a < c :
    print("Both conditions are True")


# The or Operator

# The or keyword is a logical operator, and is used to combine conditional statements. At least one condition must be true for the entire expression to be true.
print()
if b > c or  a < c :
    print("At least one of the conditions is True")


# The not Operator

# The not keyword is a logical operator, and is used to reverse the result of the conditional statement.

if not a > c :
    print("a is NOT greater than b")