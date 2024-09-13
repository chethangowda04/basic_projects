####LOCK#####
import threading
import time
class BankAccount():
    def __init__(self,name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return self.name

account1 = BankAccount("account1", 100)
account2 = BankAccount("account2", 0)

lock = threading.Lock()

class BankTransferThread(threading.Thread):
    def __init__ (self, sender, receiver,amount):
        threading.Thread.__init__(self)
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

    def run(self):
        lock.acquire()
        sender_initial_balance = self.sender.balance
        sender_initial_balance -= self.amount
        time.sleep(0.001)
        self.sender.balance = sender_initial_balance

        receiver_initial_balance = self.receiver.balance
        receiver_initial_balance += self.amount
        time.sleep(0.001)
        self.receiver.balance = receiver_initial_balance

        lock.release()

if __name__ == "__main__":
    threads = []
    for i in range (100):
        threads.append(BankTransferThread(account1, account2, 1))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print(account1.name, account1.balance)
    print(account2.name, account2.balance)

lock = threading.Lock()
x = 100
def thread_task(amt):
    time.sleep(1)
    lock.acquire()
    global x
    x = x-amt
    print(x)
    lock.release()

for i in range(10):
    t1 =  threading.Thread(target = thread_task, args = (10,))

    t1.start()
    t1.join()
