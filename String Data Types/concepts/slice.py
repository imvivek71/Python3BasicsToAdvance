# We  can access the str elements by using the slice operator

x = 'Ifyouarelearninngthisurgreat'

print(x[:])
print(x[0:7])
print(x[0:7:2])  # for accessing by gap of 2
print(x[2:])
print(x[:2])

print(x[::])   # this also works
print(x[::1])
print((x[::-1]))  # for reverse
print(x[2::])
print(x[::-2])  # for reverse by 2 gap


print(x+x)   # for addition/concatenation for this all variables should be string type

print(x*2)   # for repeat by 2 times


a ='zbcad'
b = 'zacd'
print(b>a)
print(a==b)


# Removing spaces from string
a = ' vivek '
print(a.strip())   # for removing all side spaces
print(a.rstrip())   # for right space
print(a.lstrip())  # for left space








