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

    def __instancecheck__(self, instance):
        return isinstance(instance, House)

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        else: f'Объект {other.name} принадлежит другому классу'

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        else:
            f'Объект {other.name} принадлежит другому классу'

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        else:
            f'Объект {other.name} принадлежит другому классу'

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        else:
            f'Объект {other.name} принадлежит другому классу'

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        else:
            f'Объект {other.name} принадлежит другому классу'

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        else:
            f'Объект {other.name} принадлежит другому классу'

    def __add__(self, value):
        self.number_of_floors += value
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)



h1 = House('ЖК Горский', 10)
h2 = House('Домик в деревне', 20)

print(h1)
print(h2)

print(h1 == h2)
h1 = h1+10
print(h1 == h2)

h1 = 10 + h1
print(h1)
print(h2)

print(h1 > h2)
print(h1 >= h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 != h2)
