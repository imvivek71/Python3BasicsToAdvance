"""""
Tuple is an immutable data type and all other features are same as list, but it is not growable in nature and not changeable like list

* It read only list
* Heterogeneous are allowed
* Duplicates are allowed
* Insertion order is preserved
* We can not perform append,remove,insert as in list
* Tuples are enclosed in parenthesis () separated  by comma ,

"""

t = (10,20,30,40)
print(tuple(range(1,10)))


# Single valued tuple shows the type of element

x = (0,)
print(type(x))
print(type('c'))
print(type(14,))

# Creation of tuples

t = ()  # empty tuple
t = (10,)  # single valued tuple
t = 10,20,30,40,50 # multi values tuple () optional

t = tuple(list(range(1,10)))  # By using tuple function






