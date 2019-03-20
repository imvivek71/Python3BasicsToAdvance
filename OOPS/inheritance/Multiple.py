#  A child class inheriting many parent class


class A:

    def add():
        print('It is class A')


class B:

    def sub():
        print('It is the class b')


class C(A,B):  # Inheriting the multiple class
    pass


C.sub()
C.add()
