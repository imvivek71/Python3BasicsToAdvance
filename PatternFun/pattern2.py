"""""
*****
****
***
**
*
"""

x = int(input('Enter a num' ))

for i in range(x+1):
    for j in range(x - i):
        print(' ', end='')

    for j in range(x-i):
        print('*',end='')

    print()