# union  to return all the elements present in both sets

x =set(range(0,10,2))
y = set(range(6,20,2))
print(x|y)
print(x.union(y))


# intersection of x&y will return all the common elements present in both the set

print(x.intersection(y))  # or

print(x&y)

# difference x-y returns the elements present in x but not in y

print(x.difference(y))

print(x-y)
print(y.difference(x))
print(y-x)


# symmetric difference uncommon elements in both

print(x.symmetric_difference(y))
print(x^y)


# Membership Operator in,  not in

print(10 in x)
print(10 not in x)

# Set comprehensions

s = {z*z for z in range(1,10)}
print(s)


s = {c**2 for c in range(1,10,2)}

print(s)

