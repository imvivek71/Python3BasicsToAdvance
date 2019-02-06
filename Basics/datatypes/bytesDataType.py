# A group of byte numbers  just like an array   which in range( 0 to  256)

x = [10,255, 250]
b = bytes(x)
print(type(b))
print(b[0])
print(b[-1])

# bytes doesnt support item assignment  as b[0]=10
