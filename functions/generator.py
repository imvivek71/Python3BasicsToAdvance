def generator(a):
    yield a[0]
    yield a[1]
    yield a[2]


a =[1, 2, 3]

b = generator(a)
print(next(b))

print(next(b))

print(next(b))

