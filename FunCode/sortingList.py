#  sort the a tuple

def tupleSort(a):
    print(a[::-1])   # This will give reverse of tuple/list
    print(a[::])   # this will print all elements of tuple
    print(t[:-1])  # till last one it will  print
    x = list(t)
    last =[x[-1]]
    x.remove(x[-1],)
    x.sort()
    print(last+x)



t = (1,2,3,4,4,41,2,3,22,11,12,18)
tupleSort(t)