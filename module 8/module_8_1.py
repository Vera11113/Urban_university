def add_everything_up(a, b):
    try:
        return a+b

    except TypeError:
        return str(a) + str(b)



print(add_everything_up(123.456, 'string'))
print(add_everything_up('apple', 4215))
print(add_everything_up(123.45, 7))
