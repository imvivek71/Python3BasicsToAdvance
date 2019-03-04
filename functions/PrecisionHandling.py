"""""

Python in its definition allows to handle precision of floating point numbers in several ways using different functions.
 Most of them are defined under the “math” module. Some of the most used operations are discussed in this article.

1. trunc() :- This function is used to eliminate all decimal part of the floating point number and return the integer
without the decimal part.

2. ceil() :- This function is used to print the least integer greater than the given number.

3. floor() :- This function is used to print the greatest integer smaller than the given integer.

"""

import math

x = 3.345678

print(math.trunc(x), '  ', math.floor(x), ' ', math.ceil(x))

# setting precision for float using  %, format and round

print('%2f' % x)

print('{0:.4f}'.format(x))

print(round(x, 3))


