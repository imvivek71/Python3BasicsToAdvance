#   We can have both normal and keyword  variable number arguments for only multiple we will take *args
#   and for both **kwargs


def MyFun(*n):
    for items in n:
        print(items,end=' ')


MyFun(10,12,2,23,43)
MyFun(10,12,2,23,43)




def MyFun1(**n):
    for items in n.items():
        print(items)

MyFun1(x = 'Vivek',y = 'Varsha', z = 'devloper')

# O/P  ('x', 'Vivek') ('y', 'Varsha') ('z', 'devloper')

#  MyFun1(10,x = 'Vivek',y = 'Varsha', z = 'devloper')  This does not take any positional argument