# WAP  to reverse order of words of a string


x = 'My name is Vivek Goswami'  # Desired output 'Goswami vivek is name My'

lis = x.split()
m=[]
for i in range(len(lis)):
    m.append(lis.pop())


print(' '.join(m))
