#  Partial function allow us to  modify some arguments


from functools import partial

def partialF(a,b,c,d):
    print(a,' ',b,' ', c,' ',d)


partialF(1,2,3,4)

g = partial(partialF,1,2,3)

g(5)





k = partial(partialF,a=2,b=1,c=2)

g(6)