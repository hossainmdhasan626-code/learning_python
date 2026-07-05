import json


# Python - JSON

# JSON is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript object notation.


# JSON in Python
# Python has a built-in package called json, which can be used to work with JSON data.


# Parse JSON - Convert from JSON to Python

# If you have a JSON string, you can parse it by using the json.loads() method.

a =  '{ "name":"John", "age":30, "city":"New York"}'
b = json.loads(a)
print(a)
print(b)


print("***")


# Convert from Python to JSON

# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

c = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

y = json.dumps(c)
print(y)


print("***")


# Format the Result

# The example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks.
# The json.dumps() method has parameters to make it easier to read the result
d = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(d, indent=4))


print("***")


# Order the Result

# The json.dumps() method has parameters to order the keys in the result:
print(json.dumps(d, indent=4,sort_keys=True))