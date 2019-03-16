"""""
In computer science, a symbol table is a data structure used by a language translator such as a compiler or interpreter,
 where each identifier in a program's source code is associated with information relating to its declaration or
 appearance in the source, such as its type, scope level and sometimes its location.



"""

def add():
    a= 10
    b =10

    print(locals())

add()

print(globals())

globals()['a']=100

print(a)


def odd(a):
    if a%2!=0:
        return True
a =[10,20,22,2,11,12,13,17,12,11,11,11]
z = set(filter(odd,a))

print(z)