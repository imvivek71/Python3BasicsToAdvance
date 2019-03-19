# Setting the Recursion limit for a recursive function


import sys

print(sys.getrecursionlimit())   # getting the number of limit of recursion
sys.setrecursionlimit(15)         #  setting the recursion limit

print(sys.getrecursionlimit())


def fact(a):
    if a<1:
        return 1
    return a*fact(a-1)


print(fact(10))


def greet():

    print('Hello')
    return greet()


greet()
