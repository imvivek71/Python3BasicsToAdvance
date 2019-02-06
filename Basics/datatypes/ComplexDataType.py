"""""
Complex data type contains real and imaginary form:    a+bj
  where a i s the real part and bj is imaginary part

For real form if it is in int form then we can use binary, oct,  and hex form, but  for imaginary part we can  only use   float /decimal

"""

a = 5+8j
b = 6+9j
print(a+b)
print(type(a))

# For taking real or imaginary part separately
print(a.real, ' ',  a.imag)

