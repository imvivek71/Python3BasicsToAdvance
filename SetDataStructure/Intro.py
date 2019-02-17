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

# Functions  used in set


# add(x)
s.add(30)
print(s)

# update(x,y,z) -  To add multiple values single time,  but should be iterable
ls = [23,3,44,45,45,45]
s.update(ls,range(5))
print(s)


# copy()
x =s
s1 = s.copy()
print(s1)

# pop() it removes and return some random elements

print(s.pop())
print(s)
print(s1)
print(s)

# remove() it removes some specified elements(If not will give a value error) in set

s.remove(10)
print(s)


# discard() it removes some specified elements(If not will not give an error) in set

s.discard(1)
s.discard(1)
print(s)

# clear() to remove all the elements of the set

s.clear()
print(s)
