from pprint import pprint
import io

def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding = 'utf-8')
    string_positions = {}
    for str_ in strings:
        file.write(str_+'\n')
    file.close()
    file = open(file_name, 'r', encoding = 'utf-8')
    for i  in range(len(strings)):
        str_num = i+1
        bayt_num = file.tell()
        key = (str_num, bayt_num)
        string_positions[key] = file.readline().replace('\n', '')

    return string_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
