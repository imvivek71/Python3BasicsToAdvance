import threading, time



def add():
    print('Thread started')

    time.sleep(5)

    print('t1 after 5 sec')

def sub():
    print('Thread t2 started')

    time.sleep(5)

    print('t2 afterv 5 sec')


t1 = threading.Thread(target=add)


t2 = threading.Thread(target=sub)


t1.start()  # starting thread 1
t2.start()  # starting thread 2

# Once the threads start, the current program (you can think of it like a main thread)
# also keeps on executing. In order to stop execution of current program until a thread is complete, we use join method.

t1.join()   # wait till this get
print(12345)
t2.join()   # wait till this get executed
