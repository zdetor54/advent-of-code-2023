import pandas as pd
from helper import read_file
import re


# file_path = 'input.txt'
file_path = 'test_input.txt'
lines = read_file(file_path = file_path)

records_type1 = [line.split()[0] for line in lines]

records_type2 = []

for line in lines:
    record_1, record_2 = line.split()
    temp= []
    for element in record_2.split(','):
        temp.append(int(element))
    records_type2.append(temp)


input = records_type1[0]
outputs = [input]

print(input)

options_array = []

for input in records_type1:
    outputs = [input]
    for i in range(len(input)):
        if input[i] == '?':
            new_output = []
            for output in outputs:
                new_string_dot = output[:i]+'.'+output[i+1:]
                new_string_hash = output[:i] + '#' + output[i + 1:]
                new_output.append(new_string_dot)
                new_output.append(new_string_hash)
            outputs = new_output.copy()
    options_array.append(outputs)
def get_type_2(input):
    temp = input.split('.')
    temp = [len(x) for x in temp if len(x)>0]
    return temp

total = 0
for i in range(len(records_type1)):
    expected_type_2 = records_type2[i]
    print(f'New expected: {expected_type_2}, row:{i}, total: {total}')
    for option in options_array[i]:
        # print(option)
        # print (expected_type_2, get_type_2(option), total)
        if expected_type_2 == get_type_2(option):
            total += 1

print(total)