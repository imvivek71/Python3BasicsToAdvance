"""""
WAP to accept string input and display its characters by index wise (both +ve and -ve)

"""

x = input('Enter any string')
i = 0
n = len(x)
for elements in x:
    print("The character present at positive index {} and negative index {}  is {}".format(i,i-n,elements))
    i = i+1
