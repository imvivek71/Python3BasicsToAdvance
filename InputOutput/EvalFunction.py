#  Command Line argument

#  The argument which are passing at the time of execution are command line execution

#  argv is not an array it is a list

from sys import argv


print(type(argv))
print(len(argv))
print(argv)
for x in argv:
    print(x)
