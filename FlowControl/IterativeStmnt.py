"""""
for loop - If we want to iterate till some sequence

while loop - if we want till a condition true or false


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



