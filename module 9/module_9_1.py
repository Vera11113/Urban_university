def apply_all_func(int_list, *functions):

    results = {}
    for func in functions:
        try:
            if func.__name__ == 'max':
                results[func.__name__] = max(int_list)
            if func.__name__ == 'min':
                results[func.__name__] = min(int_list)
            if func.__name__ == 'len':
                results[func.__name__] = len(int_list)
            if func.__name__ == 'sum':
                results[func.__name__] = sum(int_list)
            if func.__name__ == 'sorted':
                results[func.__name__] = sorted(int_list)
        except TypeError:
            print('Введите число')

    return results


def sum(int_list):
    sum = 0
    for i in int_list:
        sum += i
    return sum

def sorted(int_list):

    for i in range(len(int_list)):
        for j in range(i+1, len(int_list)):
            if int_list[j] < int_list[i]:
                int_list[i], int_list[j] = int_list[j], int_list[i]

    return int_list


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))

