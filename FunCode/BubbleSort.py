#  Bubble sorting is a kind of sorting in which swapping happens multiple times to swap expected right to left

def bubbleSort(l):
    n = len(l)
    for i in range(n):
        for j in range(i+1,n-1):
            if l[i]<l[j]:
                l[i],l[j]=l[j],l[i]

    print(l)
a = [1,2,3,4,4,41,2,3,22,11,12,18]

bubbleSort(a)

