#  Based on divide conquer algorithms

# binary search

def binaryserach(a,e):
    n = len(a)
    if n<1:
        return a if a==e else 'The element is not in list'

    for i in range(n):
        l = 0
        u = n-1
        if a[(l+u)//2]<e:
            l = (l+u)//2
        elif a[(l+u)//2]<e:
            u = (l+u)/2
        elif e==a[(l+u)//2]:
            return e
    return "Number is not in list"

a = [[1, 1, 2, 2, 3, 4, 4, 5, 7, 9, 329, 2323]]

print(binaryserach(a,[2323]))