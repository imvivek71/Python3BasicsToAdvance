# Accessing elements of tuple

# by using index and slice same as list

x = tuple(range(1,10))
print(x[::])
print(x[::-1])
print(x[:])

# Mathematical support + and * same as list

print(x*2)
print(x+x)

# it support len(),count(), index() same as list but it support sorted() instead of sort()

x = sorted(x,reverse=True)
print(x)


# to find min and max

print(min(x),max(x))


t = 10,120,130,5 # tuple packing

a,b,c,d, = t # tuple unpacking

print(t,a,b,c,d)


# Tuple comprehension not supported by Python

