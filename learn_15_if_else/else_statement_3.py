# Python - Else Statement 


# The Else Keyword

# The else keyword catches anything which isn't caught by the preceding conditions.
# The else statement is executed when the if condition (and any elif conditions) evaluate to False.

else_0 = 200
else_1 = 33
if else_1 > else_0 :
    print("else_1 is greater than else_0")
elif else_1 == else_0:
    print("else_0 and else_1 are equal")
else:
    print("else_0 is greater than b")


# Else Without Elif

# You can also have an else without the elif:

else_0 = 200 
else_1 = 33 
if else_1 > else_0:
    print("else_1 is greater than else_0")
else:
    print("else_1 is not greater than a")
    
# *** Note: The else statement must come last. You cannot have an elif after an else.

