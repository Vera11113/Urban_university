def get_multiplied_digits(str_number):

    str_number = str_number.replace('0', '')

    first = int(str_number[0])

    if len(str_number) <= 1:
        return int(str_number)
    else:
        return first * get_multiplied_digits(str_number[1:])


str_number_input = '40203'
print(get_multiplied_digits(str_number_input))
