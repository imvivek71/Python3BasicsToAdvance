from random import randint

a = []

n = int(input('Enter the desired number'))

for i in range(n):
    a.append(randint(1,200))

print(a)

# remove duplicate the given list a

l = [1,2,2,1,1,2,2,33,44,3]

sorta = []

for j in l:
    if j not in sorta:
        sorta.append(j)

print(sorta)

#  swap first and last value of the list a
a[0],a[len(a)-1]= a[len(a)-1],a[0]

print(a)

