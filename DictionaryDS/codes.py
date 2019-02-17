# Sum of the values of a given string


d = eval(input("Enter a dict:"))
s = sum(d.values())
print(s)

# to find number of occurrence of each letter present in a string:


z = input('enter a string')
m ={}
for x in z:
    m[x]=m.get(x,0)+1
    print(m)
for k,v in m.items():
    print(m)