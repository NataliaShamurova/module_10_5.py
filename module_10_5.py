from multiprocessing import Pool
from datetime import datetime

time_start = datetime.now()
def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            # считываем строку
            line = file.readline().strip()
            all_data.append(line)
            # прерываем цикл, если строка пустая
            if not line:
                break
    return

filenames = [f'file {number}.txt' for number in range(1, 5)]

# Линейный вызов
# for name in filenames:
#     read_info(name)
# time_end = datetime.now()
# res_time = time_end - time_start
# print(res_time)

#Многопроцессный вызов
if __name__ == "__main__":

    time_start = datetime.now()
    with Pool() as pool:
        res = pool.map(read_info, filenames)

    time_end = datetime.now()

    res_time = time_end - time_start
    print(res_time)
