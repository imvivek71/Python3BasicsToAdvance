import time
import threading
def square(numbers):
    print('Calculating Square number')
    for i in range(len(numbers)):
        #time.sleep(0.5)

        numbers[i] = i*i
    print(numbers)

def cube(numbers):

    for i in range(len(numbers)):
       # time.sleep(0.5)
        numbers[i]=i**3

    print(numbers)

numbers  = [1,2,3,4,5]
t = time.time()

t1 = threading.Thread(target=square, args=(numbers,))
t2 = threading.Thread(target=cube, args=(numbers,))


t1.start()
t2.start()

t1.join()
t2.join()

print(time.time()-t)