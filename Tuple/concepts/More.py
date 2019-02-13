# add(x) adds item to the set

s = {10,20,30}
s.add(40)
print(s)

# update(x,y,z) to add multiple items tho the set, but arguments should be iterable

l = {1,2,3,4,5,6,7}
s.update(l,range(6), range(100,105)) # arguments must be iterable
print(s)


# pop() it removes and return some random number

print(l.pop())


# copy() for cloning

l1 = l.copy()
print(l1)
l2 = l
l.add(125)
print(l,l2,l1)