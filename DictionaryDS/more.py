#  popitem() it remove an arbitrary item(key-value) and return it

d = {}
print(type(d))


d[100] = "vivek"
d[101] = "Mahesh"
d[201] = "Gnaesh"
d[10121923] = "ak"
d[123]="jk"

print(d.popitem())  # for empty dict we will get value error

print(d)


# keys() to return all the associated key

print(d.keys())


# values()  it return all the associated values related with the dict

print(d.values())


# items()  all key value in form of tuple

print(d.items())

#  copy()

d1 = d.copy()
print(d1)


# set default to set a key and value
print(d.setdefault(103,"uasusu"))
print(d)

# update all items present in a dict will get added in another one

s = {1:'12',2:'4'}
d.update(s)
print(d)
