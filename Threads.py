from threading import *
def m1():
    for i in range(1):
        print("good morning...")
def m2():
    for i in range(2):
        print("good evening...")
def m3():
    for i in range (3):
        print("good night...")
print("___________________________________________")
print("\tMultithreading")
print("____________________________________________")
t1 = Thread(target = m1, name = "morning") #name is not mandatory
t2 = Thread(target = m2, name = "evening") #name is not mandatory
t3 = Thread(target = m3, name = "night") #name is not mandatory
t1.start()
t2.start()
t3.start()



###Join in Threads####
def m1():
    for i in range(1):
        print("good morning...")
def m2():
    for i in range(2):
        print("good evening...")
def m3():
    for i in range (3):
        print("good night...")
print("___________________________________________")
print("\tMultithreading")
print("____________________________________________")
t1 = Thread(target = m1, name = "morning") #name is not mandatory
t2 = Thread(target = m2, name = "evening") #name is not mandatory
t3 = Thread(target = m3, name = "night") #name is not mandatory

t1.start() #wait untill thread 1 is finished(main and subthreads t2, t3 should wait
t1.join #start thread 2 after thread 1

t2.start() #wait untill thread 2 is finished(main and subthreads t1, t3 should wait
t2.join #start thread 3 after thread 2

t3.start() #wait untill thread 3 is finished(main and subthreads t2, t1 should wait
t3.join #end of the main thread

print("end of the main thread")


##Detection of currently executing thread####
import threading

def m1():
    tname = threading.current_thread().getName()
    print("current thread\t:",tname)
    print("good Morning")

def m2():
    tname = threading.current_thread().getName()
    print("current thread\t:",tname)
    print("good Evening")

def m3():
    tname = threading.current_thread().getName()
    print("current thread\t:",tname)
    print("good Night")

print("__________________________________________________")
print("\tFinding Current Thread - Multithreading")
print("__________________________________________________-")

t1 = Thread(target=m1, name = "Morning")
t2 = Thread(target=m2, name = "Evening")
t3 = Thread(target=m3, name = "Night")

t1.start()
t2.start()
t3.start()



##Creating threads for functions with time mentioning###
import time
def cal_square(num):
    print("calculate the square of the given number")
    for n in num:
        time.sleep(0.3)
        print("square is:", n*n)

def cal_cube(num):
    print("calculate the cube of the given number")
    for n in num:
        time.sleep(0.3)
        print("cube  is:", n*n*n)

arg = [2,3,5,7,4]
t = time.time()
cal_cube(arg)
cal_square(arg)
th1 = threading.Thread(target=cal_square, args = (arg, ))
th2 = threading.Thread(target=cal_cube, args= (arg, ))
th1.start()
th2.start()
th1.join()
th2.join()
print("total time taken by time is :", time.time() -t)
print("again executing the main thread")
print("Thread 1 and Thread 2 are finished their execution")


import _thread
import time
def my_thread(thrd_mssg,delay):
    count = 0
    while count<3:
        time.sleep(delay)
        count += 1
        print(thrd_mssg,"-------------",time.time())

try:
    _thread.start_new_thread(my_thread,("thread 1", 1))
    _thread.start_new_thread(my_thread,("thread 2", 2))
except:
    print("some error occured")

while 1:
    pass


import threading
from threading import *
import time
def calc_square(numbers, delay):
    for n in numbers:
        print(f'\n{n} ^ 2 = {n*n}')
        time.sleep(delay)

def calc_cube(numbers, delay):
    for n in numbers:
        print(f'\n{n} ^ 3 = {n*n*n}')
        time.sleep(delay)

numbers = [2,3,5,8]
square_thread = threading.Thread(target=calc_square, args=(numbers,1))
cube_thread = threading.Thread(target=calc_cube, args=(numbers,2))

square_thread.start()

cube_thread.start()

square_thread.join()
cube_thread.join()

print("thread execution done")
