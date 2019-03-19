#   Sort a given number in list\


def selection(a):
       x = len(a)
       for i in range(x):
           min_i = i
           for j in range(i+1, x):

               if a[min_i]>a[j]:
                   min_i = j
           a[i],a[min_i] = a[min_i], a[i]
       return a


m = [1,2,3,4,4,1,2,2323,329,9,7,5]

print(selection(m))

