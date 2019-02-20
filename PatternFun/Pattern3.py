"""""

    *
   * *
  * * *
 * * * *
* * * * *

"""

x = int(input('Enter a num' ))

for i in range(x+1):
    for k in range(x-i):
        print(' ',end='')

    for j in range(i):
        print(' *',end='')
    print()
