#  returning a value
# return value as a tuple


def returnF1(x = 10,y=23):
    return x,y


print(returnF1())

# For list type return


def returnF1(x = 10,y=23):
    return [x,y]


print(returnF1())

# For set type return


def returnF1(x = 10,y=23):
    return {x,y}


print(returnF1())


# For dictionary type return

def returnF1(x = 10,y=23):
    d = dict()
    d['x'] = 10
    d['y'] = 23
    return d


print(returnF1())

