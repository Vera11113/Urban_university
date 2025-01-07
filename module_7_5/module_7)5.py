import os
import time
#
# print(os.getcwd())
#
# if os.path.exists('test_os'):
#     os.chdir('test_os')
# else:
#     os.mkdir('test_os')
#     os.chdir('test_os')
#
# print(os.getcwd())
# print(os.listdir())
#
# os.chdir(r'C:\Users\Вера\Urban_university\Urban_univ_study\module 7')
# print(os.getcwd())
# file = [f for f in os.listdir() if os.path.isfile(f)]
# dirs = [d for d in os.listdir() if os.path.isdir(d)]
# print(dirs)
# print(file)
# print(os.stat(file[0]))
#
# for i in os.walk('.'):
#     print(i)
#

directory = os.getcwd()

with (open('result_module_7_5.txt', 'w', encoding='utf-8') as result_file):

    for root, dirs, files in os.walk(directory):
        for file in files[:3]: #Рассмотрим только первые 3 файла
            filepath = os.path.join(directory +'\\'+ file)
            filetime = os.path.getmtime(filepath)
            formated_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
            filesize = os.path.getsize(filepath)
            parent_dir = os.path.dirname(filepath)

            text = (f'Обнаружен файл {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: '
                    f'{formated_time}, Родительская директория: {parent_dir}')

            print(text)
            result_file.write(text + '\n')

