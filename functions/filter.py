#  We can use filter function to filter values of a given sequence based on some conditions


def fil(x):
    if x%2 ==0:
        return True
    else:
        return False

l = [1,2,3,4,5,5]

l2 = list(filter(fil,l))

print(l2)


# Using Lambda function

l3   = list(filter(lambda x:x%2==0,l))

print(l3)