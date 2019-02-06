"""""
Represents a sequence of numbers
It is immutable
No item assignment
It generates numbers for a given range

"""

r = range(10)
a = range(10,20)
print(a[0])
z = range(10,20, 2)
for i in z:print(i, end='')


# creating a list by range
x = list(range(10))
print('\n',x)