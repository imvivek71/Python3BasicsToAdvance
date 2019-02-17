# WAP to print different vowels present in the given word

w = '123efchbjerv I am the boss'
w = set(w)
v = {'a','e','o','u','i','A','E','I','O','U'}

print(w.intersection(v))


# WAP to eliminate duplicate of given list with minimum two approach

x = [1,3,4,4,4,4,32,23,32,12,33,23]
print(list(set(x)))

y =[]

for i in x:
    if i not in y:
        y.append(i)
print(y)



