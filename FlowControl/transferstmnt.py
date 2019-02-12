"""""

There are following  tarnsfer stmnts:

break: to break the loop based on some conditions
continue: to skip current iteration, we use continue
pass: if we rae using the conditional block like if & we are not using it then

"""
# Use of break statement


bag = [10,200,300,1,2,2,3,3,]
for i in bag:
    if i>=200:
        break
    print(i)

# Use of continue statement

for i in bag:
    if i>=200:
        continue
    print(i, end=' ')


# Use of pass statement

if True:pass
