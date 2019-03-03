#   We can have both normal and keyword  variable number arguments for only multiple we will take *args
#   and for both **kwargs

def MyFun(m,*n):      #  we can give arguments with *args

    for items in n:
        print(items,end=' ')

MyFun(12,2,23,43)
MyFun(10,12,2,23,43)


def MyFun1(m,**n):
    for items in n.items():
        print(items)
        print(m)
    print(n)    # Result a dictionary

MyFun1(10,x = 'Vivek',y = 'Varsha', z = 'devloper')

# O/P  ('x', 'Vivek') ('y', 'Varsha') ('z', 'devloper')

#  MyFun1(10,x = 'Vivek',y = 'Varsha', z = 'devloper')  This does not take any positional argument


def myFun3(*n,l):   # this is also valid
   print(n, l)
myFun3(1,2,3,4,l=10)


# Program to find the multiplication of any number by using a input function *args

def mult(*n):
    act =1
    if len(n)==1:
        print(n)
        return 1
    for x in n:
        act *=x
    print(act)
mult(1,2,3,4,4,4)
