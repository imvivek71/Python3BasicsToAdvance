"""""
Local variables: Which are declared with in a function called local variables, and are available for that function only
and we can not access these variables outside the function



Global variables: can get access outside of the function


"""

a = 100 # Global
def f1():
    global a  # global
    a = 10  # local variable
    print(a)

f1()

def f2():
    print(a)

def extendList(val, list=[]):
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')

print("list1 = %s" % list1)
print("list2 = %s" % list2)
print("list3 = %s" % list3)

list = ['a', 'b', 'c', 'd', 'e']
print (list[0:1000])