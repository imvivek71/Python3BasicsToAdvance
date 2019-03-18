#  Swap the 1st and last elements of list

inputList = []

num = int(input('Enter  the length of list'))
if num>1:
    for i in range(num):
        inputList.append(int(input('Enter the list elements')))
        if i == num - 1:
            inputList[i], inputList[0] = inputList[0], inputList[i]
    print(inputList)

    #  or after ending the loop

    inputList[0], inputList[len(inputList) - 1] = inputList[len(inputList) - 1], inputList[0]

    print(inputList)

else:
    print('Kindly enter a list greater than length of 1 ')
