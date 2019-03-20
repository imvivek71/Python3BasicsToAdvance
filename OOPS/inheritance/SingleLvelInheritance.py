"""""
Inheritance is defined as a way in which a particular class inherits features from its base class.
Base class is also knows as ‘Superclass’ and the class which inherits from the Superclass is knows as ‘Subclass’



"""
#  Single inheritance


class A:  # Super class
    var = 124

    def funca():
        print('Your are  calling parent class')


class B(A):  # Child class
    def funcb():
        print("You are using class B")


print(B.funca())  # Now I can use all the features of class A
print(B.funcb())
print(B.var)


