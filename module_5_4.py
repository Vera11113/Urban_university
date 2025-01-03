class House:

    house_history = []
    def __new__(cls, *args, **kwargs):
        cls.house_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, floors):
        self.name = name
        self.number_of_floors = floors


    def __del__(self):
        print(f'{self.name} снесен, но он останется в истории')


h1 = House('ЖК Эльбрус', 10)
print(House.house_history)
h2 = House('ЖК Акация', 20)
print(House.house_history)
h3 = House('ЖК Матрешки', 20)
print(House.house_history)

del h2
del h3

print(House.house_history)