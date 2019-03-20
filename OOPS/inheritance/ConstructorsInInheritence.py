#  Demonstration of constructor in inheritance

class A:

    def __init__(self):
        print('This is the constructor of parent class')


class B:
        def __init__(self):
            print('this is the cont. of B class')
        def fun():
           print('Hellow')


x = B()   # this will call the constructor of super class bcz the constructor is not in the same class


class C(A):
      def __init__(self):
         print('It is the constructor of C class')


y = C()  # this will call the constructor of same class bcz the constructor is in the same class


#  Using super.__init__() we can get the constructor of super class


class D(B, A):    # This will call constructor of B bcz it works from left to right
    def __init__(self):
        super().__init__()
        print('This is the cont. of D class')


z = D()

