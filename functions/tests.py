def even(a):
    if a == 'v':
        return True


a = [10,15,20,25,30,35,40,50]
c = 'vivekgoswami'
b = list(filter(even, c))

print(b)
x =[]
for i in a:
    if i%2==0:
        x.append(i)
print(x)

for r in a:
    if r%2!=0:
        a.remove(r)
print(a)

a = [10,15,20,25,30,35,40,50]

#print(a.remove(i for i in a))

l = list(filter(lambda a:a%2==0,a))

print(l)
