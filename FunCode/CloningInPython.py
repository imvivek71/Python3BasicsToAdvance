# Why copy

a = [1,2,3,4,[1,2,3,4],12]

b = a  # we are assigning so we are referring a to b

a.append(11)  # both a and b will get changed

print(a,b)


# so to avoid these things we should use cloning using copy module

# Normal Copy

c = [1,2,3,4,[1,2,3,4],12] # we have taken an nested list

d = c.copy()  # we just copied the original list

c.append(13)  # when we are changing something in main list then it will not reflected in copied list

print(c,d)

c[4].append(100)  # but when we are changing some thing  in original nested list  then it will get change in copied list also

print(c,d)

##########################################################################################################

# introduction of copy module shallow and deep

import copy

x=[1,2,3,4]
y = copy.copy(x)
z = copy.deepcopy(x)
x.append(10)   # For  non nested list both will work same as normal copy
print(x,y,z)


#########################################################################################

# difference between shallow and deepcopy

s = [1,2,3,4,4,4,[12,1,3,5], 19]

ss = copy.copy(s)

sd = copy.deepcopy(s)

s[6].append(18)   # in shallow copy nested elements will also get changed, but in deep copy nothing will get changed

print(s,ss,sd)
