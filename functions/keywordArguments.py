# Keyword Argument

def KeywordArgv(x,y):
    print(x,y)


KeywordArgv(x = 10, y=20)   # We are assigning the value of argument while calling
KeywordArgv(y = 10,x = 34)  # Here order of argument does not matter


# KeywordArgv(x=11, 10)   This is wrong bcz keyword argument follow keyword argument only

KeywordArgv(10, y=11)  # This will work because because simple argument can follow keyword or default argument

def Fun2(vivek, radhe = 'Ritesh'):
    print(vivek, radhe)
#  Fun2(vivek='Varsha', 'ganesh')  # non keyword or non default argument are come before keyword/default argument

Fun2(10, 'zk')

