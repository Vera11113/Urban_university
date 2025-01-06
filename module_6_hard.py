from math import pi

class Figure:

    sides_count = 0

    def __init__(self, color, *sides, filled = True):

        self.__sides = []
        for side in sides:
            self.__sides.append(side)
        self.__color = color
        self.filled = filled ##True

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        low, high = 0, 255
        in_range = all(low <= num <= high for num in [r,g,b])
        return in_range

    def set_color(self, r,g,b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *args):

        if len(args) == self.sides_count:

            is_normal = all(num > 0 and isinstance(num, int) for num in args)
            return is_normal

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = []
            for side in new_sides:
                self.__sides.append(side)

class Circle(Figure):

    sides_count = 1

    def __init__(self, color, *sides, filled = True):
        super().__init__(color, *sides, filled = filled)
        if len(self._Figure__sides) > 1:
            self._Figure__sides = [1]

        self.__radius = self._Figure__sides[0] / 2 * pi

    def get_square(self):
        return pi*(self.__radius**2)

    def get_radius(self):
        return self.__radius


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides, filled = True):
        super().__init__(color, *sides, filled = filled)
        if len(self.get_sides()) == 3:
            self._Figure__sides = self._Figure__sides
        elif len(self.get_sides()) == 1:
            self._Figure__sides = self._Figure__sides * self.sides_count
        else:
            self._Figure__sides = [1] * self.sides_count

    def get_square(self):
        p = self.__len__()
        a = self._Figure__sides[0]
        b= self._Figure__sides[1]
        c = self._Figure__sides[2]
        return (p*(p-a)*(p-b)*(p-c))**(0.5)

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides, filled = True):
        super().__init__(color, *sides, filled = filled)
        if len(self.get_sides()) == 1:
            self._Figure__sides = self._Figure__sides * self.sides_count
        elif len(self._Figure__sides) == 3:
            self._Figure__sides = self._Figure__sides * int(self.sides_count/3)
        elif len(self.get_sides()) == 12:
            self._Figure__sides = self._Figure__sides
        else:
            self._Figure__sides = [1] * self.sides_count

    def get_volume(self): ##по идее у куба все грани равны
        ## но представим, что тут еще может быть параллелепипед
        if self._Figure__sides.count(self._Figure__sides[0]) == len(self._Figure__sides):
            return self._Figure__sides[0] ** 3
        else:
            volume = 1
            unique_sides = set(self._Figure__sides)
            while unique_sides:
                volume *= unique_sides.pop()

            return volume

circle1 = Circle((200, 200, 100), 10)
print(circle1.get_radius())
cube1 = Cube((222, 35, 130), 6, 7, 9)
print(cube1.get_sides())

##Проверка на ошибки заполнения
cr2 = Circle((200, 200, 100), 10, 15, 6, filled = False)
print(cr2.get_sides())
tr1 = Triangle((200, 200, 100), 10, 6, filled = True)
print(tr1.get_sides())
tr2 = Triangle((200, 200, 100), 10, 6, 8, filled = True)
print(tr2.get_sides())
print(tr2.get_square())

#Проверка на изменение цвета
print(circle1.get_color())
circle1.set_color(55, 66, 77)
print(circle1.get_color())

print(cube1.get_color())
cube1.set_color(300, 70, 15)
print(cube1.get_color())

#Проверка на изменение сторон:
print(cube1.get_sides())
cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())

print(circle1.get_sides())
circle1.set_sides(15, 12, 13)
print(circle1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())


#Проверка периметра
print(len(circle1))
print(len(cube1))

print(cube1.get_volume())
print(circle1.get_square())


