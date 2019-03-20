# reduce function reduces sequence of elements into a single element by applying specified function

from  functools import *

l =[1,2,3,4,5,5,6,66]

l2 = reduce(lambda x,y:x+y,l)

print(l2)

