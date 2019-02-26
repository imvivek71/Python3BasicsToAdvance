

# for graceful termination of the program wee need to handle exception

print(10/2)

try:   # for risky codes
    x = 10/0
except ZeroDivisionError: # can handle both zero and value error, for handling code
   pass
finally:  # for cleaning activities
    pass
print('qwertyu')