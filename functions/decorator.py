#  Decorator is a function which is used to extend the functionality and can make changes in existing function

# it takes function as argument
# decorator chaining


def decor1(fun):

    def inner(name):
        if name=='Ashu':
            print('Good Afternoon', name)
        else:
            fun(name)
    return inner


def decor(fun):

    def inner(name):
        if name=='Vivek':
            print('Good Afternoon', name)
        else:
            fun(name)
    return inner

@decor1
@decor
def wish(name):
    return print('Good Morning', name)


wish('Ashu')





