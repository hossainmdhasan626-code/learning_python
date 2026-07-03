# Python - Shorthand If 


# If you have only one statement to execute, you can put it on the same line as the if statement.

a = 5 
b = 2 
if a > b : print("a is greater than b")

# Note: You still need the colon : after the condition.


# Short Hand If ... Else

# If you have one statement for if and one for else, you can put them on the same line using a conditional expression:

c = 2 
d =300
print("c is greater than d") if c > d else print("d is greater than c")
# This is called a conditional expression (sometimes known as a "ternary operator").


# *** variable = value_if_true if condition else value_if_false


# Assign a Value With If ... Else

# You can also use a one-line if/else to choose a value and assign it to a variable:
e = 20
f = 25
g = e if e > f else f
print(g)