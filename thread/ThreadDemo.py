import time
from threading import Thread,Lock

g_num=0
lock = Lock()
def test():
    global g_num
    lock.acquire()
    for i in range(100000000):
        g_num+=1
    lock.release()

    print("------1-------g_num=%d"%g_num)


def test1():
    global g_num
    lock.acquire()
    for i in range(100000000):
        g_num += 1
    lock.release()

    print("------2-------g_num=%d" % g_num)



t1 = Thread(target=test1)
t1.start()

t2 = Thread(target=test)
t2.start()
