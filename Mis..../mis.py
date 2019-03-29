"""""
Exception handling
while True:
    try:
        num = int(input('Enter an integer number'))
    except ValueError:  # this will get executed when exception will occur in try block
        print('You did not enter integer')
    else:
        print('Good job You entered right num, try again')
        break
    finally:
        print('This will run in case of exception or no exception')
print('End of the game')


Difference b/w constructor and Function

Return type of function is whatever given but for constructor is none
For an object multiple function but only one constructor
constructor called automatically while functions manually

"""

import copy


class test:
    def __init__(self,name): # instance variable name
        self.name = name
    def add(self):
        print(self.name)
t = test('Ram')    # parametrized
t1 = test('Seeta')


del t.name


t1.add()

#################################


class A:
    def num(self):
        self.x = 10
        self.y = 20

    def display(self):
        print(self.x+self.y)


obj = A()

obj.num()   # when we call this then display will get value of variables
obj.display()

##################################

a = [1,2,3,4,44, 5]

b = copy.deepcopy(a)
b[1] = 10
print(a)
print(b)


x = [1,2,[10,20,30,40],3,3,4,100]

y = copy.copy(x)
y[2][0] = 300

print(y)
print(x)

########################################
#  Local variables


class  Local:
    def add(self):
        a = 10
        print(a)
    def ukg(self):
        b = 11
k = Local().add()


##########################################
# multiple constructors inside a class ## only last one will get executed

class MulConstructor:
    def __init__(self,ab,c):
        self.a = a
        self.b = b
    def __init__(self,c,d):
        print('2nd constructor')

MulConstructor(11,11)  # only last one will get executed

# so python does not support multiple constructor inside it & it does not support method overloading

#######################################################

class MethodOverload:

    def add(self):
        self.a = 10
        self.b = 20
        print(self.a+self.b)


    def add(self,x):
        print('last method')


MethodOverload().add(2)  # this will execute only last one with same name


#################################################

# static method
# class method
# instance method
class Fun:
    @staticmethod
    def add():
        print('qwertyu')

    @classmethod
    def sub(cls):
        print('class method')
Fun().add()
Fun().sub()


######################################################

# sum of two numbers using class and function

class Math:
    @staticmethod
    def add(num1,num2):
        print(num1+num2)


Math().add(10, 15)


#######################################################


class Animal:
    legs = 4

    @classmethod
    def dogs(cls, name):

        print("{} walks by {} legs".format(name, Animal.legs))
        print("{} walks by {} legs".format(name, cls.legs))


Animal().dogs('Dog')

######################################################

# self deep intuition


###############################################################


# class inside a class

class Outer:
    def __init__(self):
        print('Outer')

    class Inner:
        def __init__(self):
            print('inner')
        class Inner2:
            def __init__(self):
                print('Inner2')

b = Outer()
b.Inner().Inner2()


##########################################################
#garbage collection is a assitant who is always running in the backgrond to destroy useless objects
#By default garbage collector is enabled , but we can disable also according to our requirement
#Hence garbage collector main objective is to destroy useless object so that memory may free
#if an object does not have any reference variable then that object is elligible for garbage collection
#garbage collector is module as gc
#some function to enable , disable the garbage collector
#garbage collector is automatically working in python

import gc

print(gc.isenabled())
gc.disable()
print(gc.isenabled())

gc.enable()
print(gc.isenabled())


###########################################################

# destructor

class Destructor:
    def __init__(self):
        print("Constructor calling")

    def __del__(self):
        print('Destructor calling')

des = Destructor()
des1 = des
des2 = des1
del des2


##################################################################

# pickling and unpickling or serializing and deserail....

import pickle

class Employee:
    def __init__(self,name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display(self):
        print(self.name,self.age,self.salary)

with open("file.txt", 'wb') as f:
    e = Employee('Mukesh', 40, 50000)
    g = Employee('Vivek', 23, 40000)

    pickle.dump(g, f)
    pickle.dump(e, f)

    print('Pickling is done')
with open("file.txt", 'rb') as f:
    print('Unpickling is being done')
    e= pickle.load(f)

    e.display()
    g.display()
