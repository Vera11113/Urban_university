class House:
    def __init__(self, name, floors):
        self.name = name
        self.number_of_floors = floors

    def go_to(self, new_floor):
        if (new_floor < 1) or (new_floor > self.number_of_floors):
            print('Такое этажа не существует')
        else:
            for i in range(new_floor):
                print(i+1)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'


h1 = House('ЖК Горский', 10)
h2 = House('Домик в деревне', 20)
print(h1)
print(h2)
print(len(h1))
print(len(h2))
