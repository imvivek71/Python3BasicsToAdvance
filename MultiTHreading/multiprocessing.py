#################################

import multiprocessing

def add(a,b):
    print(a+b)


def sub(a,b):
    print(a-b)

t1 = multiprocessing.Process(target=add, args=(1,2))
t2 = multiprocessing.Process(target=sub, args=(2,1))

t1.start()
t2.start()

t1.join()
t2.join()

