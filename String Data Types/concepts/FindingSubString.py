


# finding sub strings for forward direction: find(), index()

a = 'nice to meet you man'

substr = 'nice'

print(a.find(substr))  # return index of first occurrence
print(a.index(substr))  # if not available it will get value error
print(a.find('123'))   # if not available it will return -1


# finding sub strings for backward direction rfind(), rindex()

print(a.rfind('n'))
print(a.find('n'))

#  counting the number of times of given substring

print(a.count('n'))  # count is a inbuilt function for counting the occurrence of a substring

# Replacing a string with another string/elements replace(old,new,count) by replace a new object is created

print(a.replace('nice','bad',1))
print(a.replace(a[0:4], 'bad', 1))


# Splitting the strings split('separator') the default is space

print(a.split()) # this will result a list

print(type(a.split()))


# Joining of strings for joining any tuple or list

print(''.join(a.split()))
print(','.join(a.split()))  # We can use separator as ,
print(type(a))
