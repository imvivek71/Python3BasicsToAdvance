"""""
Just like every other Object Oriented Programming language Python supports classes.
Let’s look at some points on Python classes.
Classes are created by keyword class.
Attributes are the variables that belong to class.
Attributes are always public and can be accessed using dot (.) operator. Eg.: Myclass.Myattribute
A sample E.g for classes:

"""


# Here is introduction of a class

class MyClass:
    num = 100
    name = 'noname'


def Main():
    me = MyClass() # Creating an object of the class
    me.name='Vivek'
    me.num = 300
    print(me.name, me.num)


def Jal():
    print('Some')

if __name__ == '__main__':  #  Telling python that there is main in program
    Main()
