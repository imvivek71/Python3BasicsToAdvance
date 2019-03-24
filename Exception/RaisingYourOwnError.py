def color(col):
    colors = ('blue', 'black', 'red', 'green')
    if type(col) is not str:
        raise TypeError("Color should be in str only")
    if col not in colors:
        raise ValueError("Color is not in colors")
    else:
        print('Hello', col)



