# creating a dictionary

d = {}
print(type(d))


d[100] = "vivek"
d[101] = "Mahesh"
d[201] = "Gnaesh"

print(d)
print(d[100])

# Update x[key] = value

d[100] = "Adi"
print(d)

# delete

del d[100]
print(d)

# del d[100] # KeyError: 100

# get() to get the related key value

x = d.get(101)
print(x)

# pop() it will remove the entry associated with the specified key and returns the corresponding value

y = d.pop(201)

print(y)

d.clear() # to clear the dict

print(d)

