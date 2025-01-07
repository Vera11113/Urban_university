def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for num in numbers:
        try:
            result += num
        except TypeError as exp:
            print(f'Некорректный тип данных для подсчета суммы - {num}')
            incorrect_data += 1

    return result, incorrect_data


def calculate_average(numbers):
    try:
        result, incorrect_data = personal_sum(numbers)
        average = result/(len(numbers) - incorrect_data)
        return average
    except ZeroDivisionError:
        print('Деление на 0')
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None


print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "String", 3, 'One more'])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')

