"""""
If we want to represent group of unique values  as a single entity then we should go for set DS

* Insertion order is not preserved
* indexing and slicing not allowed bcz insertion order is not preserved
* Heterogeneous elements are allowed
* Mutable
* are closed by curly braces {} separated by comma
* Duplicates are not allowed
* Union insertion difference can be applied

"""

s = {10,2,3,4}
print(s)

m = set(s)
print(s)

x = {}  # empty set is treated as dict
print(type(x))
x = set()   # creating an empty set ds
print(type(x))
