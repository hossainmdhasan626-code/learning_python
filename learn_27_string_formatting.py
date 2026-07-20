# Python - String Formatting

# F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.
# Before Python 3.6 we had to use the format() method.


# F-Strings

# F-string allows you to format selected parts of a string.
# To specify a string as an f-string, simply put an f in front of the string literal, like this:


# Placeholders and Modifiers

# To format values in an f-string, add placeholders {}, a placeholder can contain variables, operations, functions, and modifiers to format the value.
a = 55
b = f"The price of this product is {a} $$$"
print(b)


print("***")


# A placeholder can also include a modifier to format the value.
# A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:
c = 59
d = f"The price is {c:.2f} dollars"
print(d)


print("***")


# Perform Operations in F-Strings

# You can perform Python operations inside the placeholders.
# You can do math operations:
e = f"The price is {200 * 4} dollars"
print(e)

# You can perform math operations on variables:

f = 59
g = 0.25
h = f"The price is {f * g} dollars"
print(h)


print("***")


# You can perform if...else statements inside the placeholders:
i = 45
j = f"It is very {"Expensive" if i > 50 else "Cheap"}"
print(j)


print("***")


# Execute Functions in F-Strings

# You can execute functions inside the placeholder:
k = "apple"
l = f"I love {k.upper()}"
print(l)