#  Hierarchy

class A:
    def a():
        print('You are using the parent A ')


class B(A):  # Inheriting class A
    pass


class C(A):  # inheriting class A
    pass


print(B.a())


print(C.a())

