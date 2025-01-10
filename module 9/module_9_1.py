def apply_all_func(int_list, *functions):

    results = {}
    for func in functions:
        try:
           results[func.__name__] = func(int_list)
        except TypeError:
            print('Введите число')

    return results



print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))

