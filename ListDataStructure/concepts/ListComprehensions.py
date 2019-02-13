# It is very easy way to create ist objects from any iterable objects(like list, tuple, dictionary and range
# based on some conditions

s = [x*x for x in range(1,11)]
print(s)

print([2**x for x in range(1,10)])

print([x*x for x in tuple(range(1,10))])

x = 'I am the man of one word'.split()
print([i[0] for i in x])
j = 'I am the man of one word'
vowel ='a e i o u'.split()
m=[]
for i in range(len(j)):
    if j[i] in vowel:
        m.append(j[i])
print(set(m))