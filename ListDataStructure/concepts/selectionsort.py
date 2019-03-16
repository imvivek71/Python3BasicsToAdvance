
def selectionsort():
    y = [10, 20, 8, 9, 11, 11, 2, 3, 4]
    length = len(y)

    for k in range(length):
        min_index = k
        for j in range(k+1,length):
            if y[min_index] > y[j]:
                min_index = j
        y[k],y[min_index]=y[min_index],y[k]
    print(y)


selectionsort()
