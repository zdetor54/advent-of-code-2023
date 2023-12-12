import pandas as pd
from helper import read_file
import re


# file_path = 'input.txt'
file_path = 'test_input.txt'

lines = read_file(file_path = file_path)

lines = [[int(y) for y in x.split()] for x in lines]

def get_differences(input):
    new_array = []
    for i in range(len(input)-1):
        new_array.append(input[i+1]-input[i])
    return new_array

def predict_next_value(input):
    array_of_differences = [input]
    next_array = input
    while len(set(next_array))>1:
        next_array = get_differences(next_array)
        array_of_differences.append(next_array)

    final_num = 0
    for line in reversed(array_of_differences):
        final_num += line[-1]

    array_of_differences[0].append(final_num)
    return array_of_differences


print(lines)

# PART 1
total_sum = 0
for line in lines[:]:
    temp = predict_next_value(line)
    print(temp)
    total_sum += temp[0][-1]
print(total_sum)


# PART 2

