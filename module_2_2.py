first, second, third = map(int, input('Введите 3 числа через пробел: ').split())

if (first == second) and (second == third):
    print(3)
elif (first == second) or (second == third) or (first == third):
    print(2)
else:
    print(0)

