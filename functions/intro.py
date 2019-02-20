"""""
If a group of statements required repeatdly thrn it is not required to write it again & we can define these as a single
unit and we can call these unit any times and this unit is called function(in other lang. are known as methods,procedures, subroutines)


* code reusability

There are two types of functions Built in(len(),type()) and user defined


A group of lines with some name is called function
A group of functions save to a file called Module
A group of modules is nothing just a library

"""

# User defined - The functions developed explicitly according to needs


# Parameters are inputs to the function. If a function contains parameters then at the time of calling, compulsory
# we should provide values

def wish(name):
  print("hellow",name,"GM")
wish('Vivek')


def square(number):
    print("Square of ",number," is ",number*number)

square(12)

# Return Statement

def add(a,b):
    return a+b
add(1,2)

print("The sum of numbers ", add(10,11) )


# function for checking whether it is odd or even

def even_odd(num):
    if num%2==0:
        return "Num is even "
    else:
        return "num is odd"
print(even_odd(15))


# function for factorial of the number:

def factorial(num):
    fact = 1
    while num>=1:
        fact = fact*num
        num = num-1
    return fact
print(factorial(0))

#  returning multiple values from a function
def factorial(num):
    fact = 1
    while num>=1:
        fact = fact*num
        num = num-1
    return fact, num
print(factorial(0))
