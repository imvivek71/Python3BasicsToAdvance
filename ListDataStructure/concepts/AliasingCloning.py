#  The process of giving another reference variable to the existing list is called

x =list(range(1,20))
y = x

print(id(x))
print(id(y))


y[1] = 77
print(x,y)  # same value,  so this is the problem while we are aliasing due to this our both list are being changed

# Due to this if we are changing the content then, those changes will be reflected to other reference values also
# To overcome with this problem we go for cloning , the process of creating exactly duplicate independent object


m = list(range(1,10))
n = m[:]  # cloning by using index
o = m.copy()  # cloning by using copy function method
n[1] = 100
print(m,n,o)

