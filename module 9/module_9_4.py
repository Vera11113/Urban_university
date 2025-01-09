from random import randint


"""
    Lambda - функция
"""


first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda x, y: x==y, first, second)))


""" 
    Замыкание
"""

def get_advanced_writer(file_name):

    try:
        file = open(file_name, 'a', encoding = 'utf-8')
        def write_everything(*data_set):
            for data in data_set:
                file.write(str(data) + '\n')


        return write_everything

    except:
       file.open(file_name, 'w')

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

class MysticBall:

    def __init__(self, *word):
        self.word = word

    def __call__(self):
        return self.word[randint(0, len(self.word))-1]


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())