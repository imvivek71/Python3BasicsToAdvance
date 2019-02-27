"""""
To perform file related I/O operations we use this


"""

f = open('abc.txt','w') # this will open the file for write option, if file available then its cool, otherwise this will create a file
f.write('Vivek ')     # in this form data is considered as string form only
f.write('Kumar \n')
f.write('Goswami')
f.close()


x = open('abc.txt') # reading data
data = x.read()
print(data)





