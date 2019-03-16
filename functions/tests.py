def even(a):
    if a%2==0:
        return True
    else:
        return False


a = [10,15,20,25,30,35,40,50]
b = list(filter(even, a))

x = [10,15,20,25,30,35,40,50]

for r in a:
    if r%2!=0:
        a.remove(r)
print(a)

a = [10,15,20,25,30,35,40,50]


l = list(filter(lambda a:a%2==0,a))

print(l)
