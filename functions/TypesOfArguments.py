

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




# Variable Length arguments






