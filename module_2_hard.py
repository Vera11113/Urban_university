n = int(input('Введите первое число (от 3 до 20): '))

password = ''


for i in range(1, n):
    if n < 3:
        print('Число меньше 3, пароль подобрать невозможно')
        break
    if n > 20:
        print('Число больше 20, пароль подобрать невозможно')
        break
    for j in range(i+1, n):
        if n % (i+j) == 0:
            password += str(i)+str(j)

print('Пароль: ', password)