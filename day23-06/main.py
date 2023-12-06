import pandas as pd
from helper import read_file

file_path = 'input.txt'
# file_path = 'test_input.txt'

lines = read_file(file_path = file_path)

def calculate_options (time, distance):
    result = 1
    for i in range(len(time)):
        total_time = time[i]
        total_distance = distance[i]
        # print(f'Time: {total_time}, distance: {total_distance}')

        counter = 0
        for j in range(total_time):
            if j*(total_time-j) > total_distance:
                counter += 1
        # print(counter)
        result *= counter

    print(result)





# PART 1

time = [int(x) for x in lines[0].split()[1:]]
distance = [int(x) for x in lines[1].split()[1:]]

calculate_options (time, distance)

# PART 2
time = [x for x in lines[0].split()[1:]]
distance = [x for x in lines[1].split()[1:]]

time = [int(''.join(time))]
distance = [int(''.join(distance))]

calculate_options (time, distance)
