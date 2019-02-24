"""""
Pass by value or pass by reference

One important thing to note is, in Python every variable name is a reference.
 When we pass a variable to a function, a new reference to the object is created.
 Parameter passing in Python is same as reference passing in Java.


"""
def Myfun(x): # Here x is a same reference to  list

    x[0]=20
lst = [10,10,1,1]
# after function call.

Myfun(lst);
print(lst)

# Another example

def Myfun2(x):


    # After below line link of x with previous

    # object gets broken. A new object is assigned
    # to x.

    x = [10, 11, 12, 13, 14, 15]
lst = [10, 11, 12, 13, 14,13,1,3,22123,2]
Myfun2(lst)
print(lst)  # reference link is broken if we assign a new value (inside the function).





