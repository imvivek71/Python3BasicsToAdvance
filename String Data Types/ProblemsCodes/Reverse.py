"""""
Input = 'Vivek Kumar Goswami'
Output = 'KeviV ramuK imawsoG'
"""
x = 'Vivek Kumar Goswami'
lis = x.split()
m = []
for i in range(len(lis)):
    m.append(lis[i][::-1])

print(' '.join(m))