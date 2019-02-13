# Check whether all number in a list are fibonacci or not

import math

def isfib(lis):
     count = 0
     for i in range(len(lis)):
         n = lis[i]
         if (n == 0) or (math.sqrt(5*n*n-4)- math.floor(math.sqrt(5*n*n-4)) == 0) or (math.sqrt(5*n*n+4) - math.floor(math.sqrt(5*n*n+4)) == 0) :
            count = count
         else:
             return 'ALl elements are  not fibonacci num'
     if count==0:
          return  'All elements of the list are fibonacci num'

lis =[0,1,1,2,3,5,8,13,14]
print(isfib(lis))
