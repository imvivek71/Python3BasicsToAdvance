"""""
*****
****
***
**
*
"""

x = int(input('Enter a num 1,2 or 3'))

for i in range(x+1):
    for j in range(x-i):
        print('*',end='')
    print()
