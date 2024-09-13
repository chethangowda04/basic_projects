####semaphore####
from threading import *
import time
s = Semaphore(3)
def call_names(name, age):
    for i in range(3):
        s.acquire()
        print("hi", name)
        time.sleep(2)
        s.release()

t1 = Thread(target = call_names, args = ("Chethan",23))
t2 = Thread(target = call_names, args = ("Abhishek",21))
t3 = Thread(target = call_names, args = ("Dinesh",22))
t4 = Thread(target = call_names, args = ("Manoj",24))

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()
