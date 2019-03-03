# When the default value of the argument is given is known as default valued arguments.

def MyFun(y,m,x=120): #  default arguments never follow non-default argument
    print(x,y,m)

MyFun(10,30,11)


def MyFun2(a=10,b=11,c=12):
    print(a,b,c)

MyFun2()

