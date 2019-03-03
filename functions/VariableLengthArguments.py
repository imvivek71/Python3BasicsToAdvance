#   We can have both normal and keyword  variable number arguments for only multiple we will take *args
#   and for both **kwargs

def MyFun(m =10,*n):      #  we can give arguments with *args

    for items in n:
        print(items,end=' ')

MyFun(12,2,23,43)
MyFun(10,12,2,23,43)


def MyFun1(m,**n):
    for items in n.items():
        print(items)
        print(m)
    print(n)    # Result a dictionary

MyFun1(x = 'Vivek',y = 'Varsha', z = 'devloper')

# O/P  ('x', 'Vivek') ('y', 'Varsha') ('z', 'devloper')

#  MyFun1(10,x = 'Vivek',y = 'Varsha', z = 'devloper')  This does not take any positional argument


def MyFun3(*n,l):   # this is also valid
   print(n, l)
MyFun3(1,2,3,4,l=10)

