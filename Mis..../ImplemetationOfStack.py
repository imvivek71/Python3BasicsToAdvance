"""""
Principle of “Last-in, first-out”, to push an item, we use append() function and to pop out an element we use pop() function


"""

stack = ['A', 'B', 'C']
stack.append('D')  # pushing an item

stack.append('E')  # pushing an item

print(stack)

print(stack.pop())
print(stack)

print(stack.pop())
print(stack)

