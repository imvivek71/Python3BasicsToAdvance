"""""
List data Type: It represent  a group of values as single entity where insertion order required to preserve and duplicates

and duplicates are allowed.

Insertion order is preserved
Heterogeneous objects are allowed
Duplicate are allowed
Grow able in nature
Values Should be enclosed in square brackets
"""

list = [10,12,'vivek',13]
list[0]
list[0]=28 # support item assignment
list[1:3] # will print 12,vivek

# We can  increase or decrease the size
list.append("ashu")
print(list)
list.remove(list[2])
print(list)

# an ordered, mutable, heterogeneous, collection of elements where duplicates ar allowed is called list. .


