import threading, time,os



def add():
    print('Thread started',' current thread name {} and process {}'.format(threading.current_thread(), os.getegid()))

    time.sleep(5)

    print('t1 after 5 sec',' currentb thread name {} '.format(threading.current_thread()))

def sub():
    print('Thread t2 started' ,' current thread name {} '.format(threading.current_thread()))

    time.sleep(5)

    print('t2 afterv 5 sec',' current thread name {} '.format(threading.current_thread()))


t1 = threading.Thread(target=add)


t2 = threading.Thread(target=sub)


t1.start()  # starting thread 1
t2.start()  # starting thread 2

print(t1.is_alive())
print(t2.is_alive())
# Once the threads start, the current program (you can think of it like a main thread)
# also keeps on executing. In order to stop execution of current program until a thread is complete, we use join method.

t1.join()   # wait till this get
print(12345)
t2.join()   # wait till this get executed


print(t1.is_alive())
print(t2.is_alive())