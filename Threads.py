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