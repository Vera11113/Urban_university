import threading
from time import sleep
from random import randint
from queue import Queue

class Table:

    def __init__(self, number, guest = None):
        self.number = number
        self.guest = guest

class Guest(threading.Thread):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.sitted = False

    def run(self):
        super().run()
        time = randint(3, 10)
        sleep(time)

class Cafe:

    def __init__(self, *tables):
        self.q = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for guest in guests:
            sleep(0.5)
            for table in self.tables:
                if table.guest == None:
                    table.guest = guest
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    table.guest.sitted = True
                    table.guest.start()
                    break
            if guest.sitted == False:
                self.q.put(guest)
                print(f'{guest.name} в очереди')

    def find_empty_table(self):
        return any(table.guest != None for table in self.tables)

    def discuss_guests(self):

        while not(self.q.empty()) or self.find_empty_table():
            for table in self.tables:
                if table.guest == None:
                    if not (self.q.empty()):
                        table.guest = self.q.get()
                        print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                        table.guest.start()
                    else:
                        continue
                else:
                    if not(table.guest.is_alive()):
                        print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                        print(f'Стол номер {table.number} свободен')
                        table.guest = None
                    else: continue

                    if table.guest == None:
                        if not(self.q.empty()):
                            table.guest = self.q.get()
                            print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                            table.guest.start()
                        else: continue

            sleep(1)


tables = [Table(number) for number in range(1, 6)]
guests_names = [ 'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']

guests = [Guest(name) for name in guests_names]
cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
cafe.discuss_guests()