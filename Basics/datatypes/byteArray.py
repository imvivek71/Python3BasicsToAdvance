# A group of byte numbers  just like an array   which in range( 0 to  256)
# It is  same as bytes array type but  it support item assignment  as b[0]=10
x = [10,255, 250]
b = bytearray(x)
print(type(b))
b[0] = 20
print(b[0])
print(b[-1])

for i in b: print(i)