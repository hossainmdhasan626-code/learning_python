import sys
# Python - Recursion 

# Recursion is when a function calls itself.
# Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.
# The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. 
# However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.
def count_down(n):
    if n <= 0: # Base case
        print("Done")
    else: 
        print(n) # Recursive case
        count_down(n - 1)
    
count_down(5)


print("***")


# Base Case and Recursive Case

# Every recursive function must have two parts:
#     ***A base case - A condition that stops the recursion
#     ***A recursive case - The function calling itself with a modified argument
# Without a base case, the function would call itself forever, causing a stack overflow error.



# Recursion Depth Limit

# Check the recursion limit:
print(sys.getrecursionlimit())

# If you need deeper recursion, you can increase the limit, but be careful as this can cause crashes:
sys.setrecursionlimit(2000) # Increasing the recursion limit should be done with caution. For very deep recursion, consider using iteration instead.
print(sys.getrecursionlimit())