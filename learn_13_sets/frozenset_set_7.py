# Python frozenset


# frozenset is an immutable version of a set.
# Like sets, it contains unique, unordered, unchangeable elements.
# Unlike sets, elements cannot be added or removed from a frozenset.


# Creating a frozenset

# Use the frozenset() constructor to create a frozenset from any iterable.

this_froz = frozenset({"apple", "banana", "cherry"})
print(this_froz)
print(type(this_froz))