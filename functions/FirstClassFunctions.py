"""""
A function is an instance of the Object type.
You can store the function in a variable.
You can pass the function as a parameter to another function.
You can return the function from a function.
You can store them in data structures such as hash tables, lists, …

"""
# Returning a function


def create_adder(x):
    def adder(y):
        return x + y
    return adder


add_15 = create_adder(15)


print(add_15(10))

# Functions can be passed as an argument to another function


def fun1(text):
    return text.upper()


def fun2(text):
    return text.lower()


def greet(func):
    greeting = func('Functions can be passed as an argument to another function')
    print(greeting)


greet(fun1)
greet(fun2)

# Functions are object

new = greet  # we can assign to another variable & it will not get called

new(fun1)
