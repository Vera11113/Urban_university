def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(a = 'print', c = 4)
print_params()
print_params('ok', 'no')
print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = [10, 20, 30]
values_dict = {'a': 10, 'b': 'cat', 'c': 30}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'dog']
print_params(*values_list_2, 42)