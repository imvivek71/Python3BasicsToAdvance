#  Yield vs return


def SimpleGen():
    yield 1
    yield 2
    yield 4
    yield 5
for value in SimpleGen():
    print(value)


def Return():
    return 1
print(Return())


#  Prograam for printiing 1 to 20 numbers

def Num1To20():
    for i in range(1,11):
        yield i
for k in Num1To20():
    print(k,end=' ')