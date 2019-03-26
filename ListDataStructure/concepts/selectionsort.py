
def selectionsort():
    y = [1,2,3,4,4,1,2,2323,329,9,7,5]
    length = len(y)

    for k in range(length):
        min_index = k
        for j in range(k+1,length):
            if y[min_index] > y[j]:
                min_index = j
        y[k],y[min_index]=y[min_index],y[k]
    print(y)


selectionsort()

