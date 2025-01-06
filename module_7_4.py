team1_num = 5
team2_num = 7
score_1 = 42
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2

#Использование %
print('В команде Мастера кода участников: %d!' % (team1_num))
print('Итого сегодня в командах участников: %d и %d!' % (team1_num, team2_num))

#Использование format
print('Команда Волшебники данных решила задач: {}!'.format(score_2))
print('Волшебники данных решили задачи за {:.2f}с!'.format(team2_time))

#Использование f-строк
print(f'Команды решили {score_1} и {score_2} задач.')

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'победа команды Волшебники данных!'
else: result = 'ничья!'

print(f'Результат битвы: {result}')


