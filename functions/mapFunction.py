#  Map function : For every element present in the given sequence apply some  funtionality and generate new element with
#  required modifications


# syntax: map(function,sequence)

def mapping(x):
    return 2*x

l = [1,2,3,4,4,5]

l2 = list(map(mapping, l))

print(l2)

# using lambda function


l3 = list(map(lambda x:2*x, l))

print(l3)