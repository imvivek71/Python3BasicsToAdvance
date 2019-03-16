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