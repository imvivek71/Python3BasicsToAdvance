# Ordering a list


# Reverse

x = [1,2,3,4,5,6]
x.reverse()
print(x)
print(x[::-1])
y = []
for i in range(len(x)):
    y.append(x.pop())
print(y)


# sorting for sorting elements should homogeneous

lis = [10,6,9,98,6,4,210,1,]
lis.sort()
print(lis)
lis1 =('i am not a gentle man').split()
lis1.sort(reverse=True)  # For reverse sort we should use reverse= True, by default sorting is in ascending order
print(lis1)

