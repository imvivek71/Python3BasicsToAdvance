

def add(a,b):
    print( a-b)
add(1,2)

# in the above example a,b are formal arguments and 1,2 are actual arguments
# There are 4 types of arguments positional, keyword, default and variable length argmnts

# positional arguments : These are the arguments passed to function in correct positional order
# number of arguments and position  must be matched otherwise results may change

def add(a,b):
    print( a-b)
add(2,1)

# add(2,1,1) : We will get an error due change of noo. of argmnts




# Keyword Arguments: We can pass argumment values by keyword by parameter name

def add(a,b):
    print( a-b)
add(b= 18, a =20)  # here the order is not important

add(10,b=5)
# add(a=10,3) invalid





# Default arrguments we can provide default values

def greet(name = "morning"): # after taking default arg we should not take non-default argmnt as def greet(name = "morning",place)
    print("Hii ", name )

greet() # this will take default argmnt
greet("afternoon") # after giving it take this argmnt

#def greet(name = "morning",place): # invalid

def greet(place,name="morning"): #valid
    pass




# Variable Length arguments we can call this function by passing any number of arguments including zero number

# internally all values represented in form of tuple

def Mult(*n):
    result = 1
    for x in n:
        result = result*x
    print(result)

Mult(10,10)
Mult(12,1,21,12,2)


# We can mix variable length argmnt with positional:


def Mult(n1, *s):
    result = 1
    for x in s:
        result = result*x
    print(result)

Mult(10,20,30,20)


# After variable length argmnt if we are taking any other argmnt then we should give keyword type argmnts otherwise error

def Mult2(*s,n1):
    result = 1
    for x in s:
        result = result*x
    print(result)

Mult2(10,20,30,20, n1=20)





