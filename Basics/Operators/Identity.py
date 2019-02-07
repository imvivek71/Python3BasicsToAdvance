"""""
For content comparision we use ==

and for address comparision we use  is , is not


"""


a = 10.5
b = 10.5
print(a is b)
print(a is not b)

x = 5+6j
z = 5+6j

print(x is z)
print(x is not z)

m = list(range(10))
n = list(range(10))

print(m is n)

print(m[0] is n[0])
