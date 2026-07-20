# Pyton - While Loops


# The while Loop

# With the while loop we can execute a set of statements as long as a condition is true.
a = 1 
while a < 6 :
    print(a)
    a += 1
# The while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 1.

print("***")

# The break Statement

# With the break statement we can stop the loop even if the while condition is true:
b = 1 
while b < 6:
    print(b)
    if b == 3:
        break
    b += 1


print("***")


# The continue Statement

# With the continue statement we can stop the current iteration, and continue with the next:

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


print("***")


# The else Statement

# With the else statement we can run a block of code once when the condition no longer is true:
c = 1 
while c < 6 :
    print(c)
    c += 1 
else: # *** Note: The else block will NOT be executed if the loop is stopped by a break statement.
    print("c is no longer less than 6")