def generator(a):
    yield a[0]
    yield a[1]
    yield a[2]

a =[1, 2, 3]

b = list(generator(a))

print(next(generator(a)), next(generator(a)), next(generator(a)))


print(b)

