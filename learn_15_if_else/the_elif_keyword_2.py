# The Elif Keyword

# The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
# The elif keyword allows you to check multiple expressions for True and execute a block of code as soon as one of the conditions evaluates to True.

this_elif = 33
this_elif_1 = 33
if this_elif_1 > this_elif :
    print("this_elif is greater than this_elif_1")
elif this_elif == this_elif_1:
    print("this_elif and this_elif_1 are equal")
# In this example this_elif is equal to this_elif_1, so the first condition is not true, but the elif condition is true, so we print to screen that "this_elif and this_elif_1 are equal".


# Multiple Elif Statements

# You can have as many elif statements as you need. Python will check each condition in order and execute the first one that is true.
score = 75

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")
#   In this example, the program checks each condition in order. Since score is 75, it prints "Grade: C" (the first condition that evaluates to true).


# How Elif Works

# When you use elif, Python evaluates the conditions from top to bottom. As soon as it finds a condition that is true, it executes that block and skips all remaining conditions.
# *** Important: Only the first true condition will be executed. Even if multiple conditions are true, Python stops after executing the first matching block.
age = 25

if age < 13:
  print("You are a child")
elif age < 20:
  print("You are a teenager")
elif age < 65:
  print("You are an adult")
elif age >= 65:
  print("You are a senior")



# When to Use Elif
# Use elif when you have multiple mutually exclusive conditions to check. This is more efficient than using multiple separate if statements because Python stops checking once it finds a true condition.

