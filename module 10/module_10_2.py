from time import sleep
import threading

class Knight(threading.Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.evils = 100
        self.counter = 0


    def fight(self):

        while self.evils:
            sleep(1)
            self.evils -= self.power
            self.counter += 1
            print(f'{self.name} сражается {self.counter} день(дня), осталось {self.evils} воинов')

    def run(self):
        print(f'{self.name}, на нас напали!')
        self.fight()
        print(f'{self.name} одержал победу спустя {self.counter} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()



