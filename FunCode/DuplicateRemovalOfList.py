#   Remove the duplicate item from a list

#   Using only one loop If we are suppose to take input from keyboard by user


num = int(input('Enter the length of the list'))
a = []
for i in range(num):
    x = int(input('Enter the number'))
    if x not in a:
         a.append(x)

print(a)


# Using set function one line code but o/p will come in set data type

print(set(a))

