"""""
If we want to represent a group of individual object as a single entity  where insertion order is preserved and duplicates are allowed
then we should go for  a list

* Insertion order is preserved
* Heterogeneous elements are allowed
* Duplicates are allowed
* Mutable
* Dynamic type bcz as per need we can increase/decrease size of the list
* Enclosed within a bracket []

"""

# Making a list of str

x = '12345'
print(list(x))


# Nested list

y  = [1,2 ,3,4,5,[1,2,3]]
print(y[-1])
print(len(y))

# Mutability

y[1] = 100
y.append(5)
y.remove(y[0])
print(y)

# Traversing the elements of the list
i = 0
while i<len(y):
    print(y[i])
    i = i+1


# count()

print(y.count(5))


# index()

print(y.index(5))


# insert()

y.insert(0,300)
print(y)


# extend

lis1 = [1,2,3,4,5]
list2 = [1,2,3,4,5,5,6]
lis1.extend(list2)
print(lis1)

#  remove(): to remove specific item and pop() to remove last item and return that


