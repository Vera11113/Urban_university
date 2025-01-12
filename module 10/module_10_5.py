import multiprocessing
import os
import time

def read_info(filename):

    all_data = []
    with open(filename, 'r', encoding='utf-8') as file:
        while file.readline():
            all_data.append(file.readline())

if __name__ == '__main__':

    file_list = [i for i in os.listdir() if '.txt' in i]

    time_start = time.time()
    for file in file_list:
        read_info(file)
    time_stop = time.time()
    print('Время линейного считывания: ', (time_stop - time_start)) #5.36


    time_start = time.time()
    process1 = multiprocessing.Process(target = read_info, args = (file_list[0], ))
    process2 = multiprocessing.Process(target = read_info, args = (file_list[1], ))
    process3 = multiprocessing.Process(target = read_info, args = (file_list[2], ))
    process4 = multiprocessing.Process(target = read_info, args = (file_list[3], ))
    process1.start()
    process2.start()
    process3.start()
    process4.start()

    time_stop = time.time()
    print('Время процессорного считывания: ', (time_stop - time_start)) #0.09

    time_start = time.time()
    with multiprocessing.Pool(6) as p:
        p.map(read_info, file_list)

    time_stop = time.time()
    print('Время процессорного считывания: ', (time_stop - time_start)) ##2.17



