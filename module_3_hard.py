def check_list(new_list):
    if any(isinstance(elem, (list, dict, set, tuple)) for elem in new_list):
        new_list_1 = creat_new_list(new_list)
        return check_list(new_list_1)
    else: return new_list


def creat_new_list(structure):
    new_list = []
    for struc in structure:
        if isinstance(struc, dict):
            for key, value in struc.items():
                new_list.extend([key, value])

        elif isinstance(struc, set):
            a = struc.pop()
            new_list.extend(a)
        elif isinstance(struc, (int, float)):
            new_list.append(struc)
        else:
            new_list.extend(struc)

    return new_list

def calculate_structure_sum(*args):
    my_list = check_list(args)
    sum = 0
    for elem in my_list:
        if isinstance(elem, (int, float)):
            sum += elem
        else: sum += len(elem)
    return sum


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]


print(calculate_structure_sum(*data_structure))




