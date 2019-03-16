

def bubbleSort():
    x = [10, 20, 8, 9, 11, 11, 2, 3, 4]
    length = len(x)

    for i in range(length):
        for j in range(i + 1, length):
            if x[i] > x[j]:
                x[i], x[j] = x[j], x[i]
    print(x)
bubbleSort()
