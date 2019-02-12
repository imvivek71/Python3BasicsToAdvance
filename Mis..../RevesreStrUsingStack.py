

b = '1qw 89'  # Taking a string
a = list(b)   # Converting it in list

i = len(a)
c = ''        # Creating a empty string
for j in range(i):
    c+= a.pop()   # pop method for taking last element out
print(c)
