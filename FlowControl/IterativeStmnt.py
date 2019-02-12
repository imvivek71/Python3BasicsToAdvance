"""""
for loop - If we want to iterate till some sequence /Repeat code for every time in sequence

while loop - if we want till a condition true or false/ Repeat code as long as condition is true


"""

x = input('enter a string')

for i in x:
    print(i,end=' ')

while x<='10':
    print()




# Nested loop

for i in range(10):
    for j in range(i):
        print('*', end='')
    print()


# Infinite loop
k = input('enter')


while True:
    print("Infinite loop")



