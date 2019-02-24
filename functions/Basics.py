"""""
Recursive Function

When a function call himself till a certain condition, is known as recursion

In following example You can see the example of a factorial using recursion


"""

def Recursion(num):
    if num ==1 or num ==0:
        return 1
    else:
        return num*Recursion(num-1)

num = int(input('Enter any number for factorial'))

print(Recursion(num))

