import threading
import random
from time import sleep

class Bank:

    def __init__(self, balance = 0):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            increase = random.randint(50, 500)
            self.balance += increase
            print(f'Пополнение: {increase}. Баланс: {self.balance}')
            sleep(0.001)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()

    def take(self):
        for i in range(100):
            decrease = random.randint(50, 500)
            print(f'Запрос на {decrease}')
            if self.balance >= decrease:
                self.balance -= decrease
                print(f'Снятие: {decrease}. Баланс: {self.balance}')
            else:
                print('Запрос отклонен, недостаточно средств')
                self.lock.acquire()

bk = Bank()

th1 = threading.Thread(target = bk.deposit)
th2 = threading.Thread(target = bk.take)

th1.start()
th2.start()
th1.join()
th2.join()


print(f'Итоговый баланс: {bk.balance}')






