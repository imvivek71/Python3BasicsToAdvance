import functools, math
a = input('Enter the numbers separated by space').split()


def add(x):
    return int(x)+5


b = list((map(add, a)))
c = functools.reduce(lambda x,y:x+y, b)

print(b,' ',c)
###################################

# Precision handling

x = 3.45678

print(math.floor(x))
print(math.trunc(x))
print(math.ceil(x))
print('%.2f'%x)
print("{:.2f}".format(x))
print(round(x, 2))
