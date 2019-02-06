"""""
We can use  int type  to represent whole numbers.(integral values)
We can represent  in following ways:

Decimlal
Binary
Hexa
Octal


"""

# Decimal type Base 10 allowed digits 0-9
a = 10
print(a)
# Binary type base 2  0 or 1,  we should add prefix 0b or 0B

b = 0B100
b = 0b100
print(b)

# Octal  type bse  8 , 0 to 7// prefix 0O or 0o

c = 0O100
c = 0o100
print(c)

# Hexa type base 16  0 to9  & a to f (both upper and lower case )// prefix 0X or 0x
d  = 0XFACE
d = 0xface
print(d)

# base conversions there  are  inbuilt functions bin(), hex(), oct(), to convert from any base.
print(bin(0xface))

print(hex(0b100))

print(oct(0xface))

