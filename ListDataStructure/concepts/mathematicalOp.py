#  + & * operator for list

# concatenate +

x = list(range(1,5))
y = list(range(1,10))
print(x+y)

# repeat *

print(x*3)


# comparision it will check number of elements, order of elements and content

print(x==y)

# When we are using relational operators  bw list obejcts then only first element comparision is performed

x= [10,20,100]
y = [20,30,10]
print(x>y,x<y)

# membership operator
print(10 in x, 12 not in x)

# clear() tor emove all element of a list

cle = [1,2,3,3,4]
cle.clear()
print(cle)


# Nested

nested = [1,2,3,4,5,[10,20,12]]
print(nested)
print(nested[5][1])



# Nested list as a matrix

matrix = [[1,2,3,4],[1,2,3,4],[4,5,6,7],[8,9,10,11]]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j],end = ' ')
    print()