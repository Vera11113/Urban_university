class Vehicle:

    _COLOR_VARIANTS = ['blue', 'white', 'black', 'gray']

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        print(f'Модель: {self.__model}')

    def get_horsepower(self):
        print(f'Мощность двигателя: {self.__engine_power}')

    def get_color(self):
        print(f'Цвет: {self.__color}')

    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        flag = False
        for color in self._COLOR_VARIANTS:
            if new_color.lower() == color.lower():
                flag = True
        if flag:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')



class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('Black')
vehicle1.owner = 'Vasya'

vehicle1.print_info()

