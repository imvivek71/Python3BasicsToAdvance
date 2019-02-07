"""""
A module is a collection  of functions,  variables and classes etc

math is a module that contain several functions to perform mathematical operations

first we have to import after that we can function do mathematical operations

"""

import math as m  # We can import as it is or we can replace a module name by a variable
print(m.sqrt(16))
print(m.pi)

# we can directly import a function from a module as follows, so in this case it is not required to use module name math

from math import sqrt, pi

print(sqrt(25), '', pi)

print(m.factorial(5))

print(m.tan(45))


print(m.sin(30))

print(m.pow(2,3))

print(m.pi*16**16)
