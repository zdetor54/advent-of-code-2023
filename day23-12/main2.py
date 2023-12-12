import pandas as pd
from helper import read_file
from datetime import datetime


# file_path = 'input.txt'
file_path = 'test_input.txt'

lines = read_file(file_path=file_path)

records_type1 = [line.split()[0] for line in lines]

records_type2 = []

for line in lines:
    record_1, record_2 = line.split()
    temp = []
    for element in record_2.split(','):
        temp.append(int(element))
    records_type2.append(temp)

# Expand the input
for i in range(len(records_type1)):
    string_to_repeat = records_type1[i]
    list_to_repeat =  records_type2[i].copy()
    for n in range(4):
        records_type1[i] += ('?' + string_to_repeat)
        records_type2[i] += list_to_repeat


total = 0


def get_type_2(input):
    temp = input.split('.')
    temp = [len(x) for x in temp if len(x) > 0]
    return temp


for n in range(len(records_type1)):
    outputs = [records_type1[n]]
    for i in range(len(records_type1[n])):
        if records_type1[n][i] == '?':
            new_output = []
            for output in outputs:
                new_string_dot = output[:i] + '.' + output[i + 1:]
                new_string_hash = output[:i] + '#' + output[i + 1:]
                new_output.append(new_string_dot)
                new_output.append(new_string_hash)
            outputs = new_output.copy()

    expected_type_2 = records_type2[n]
    print(f'New expected: {expected_type_2}, row:{n}, total: {total} - {datetime.now().hour}:{datetime.now().minute}')
    for option in outputs:
        # print(option)
        # print (expected_type_2, get_type_2(option), total)
        if expected_type_2 == get_type_2(option):
            total += 1

print(total)
