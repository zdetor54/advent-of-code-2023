import pandas as pd
from helper import read_file

file_path = 'input.txt'
# file_path = 'test_input.txt'

points = []
lines = read_file(file_path = file_path)
numbers = []

def find_symbols(lines):
    symbols =set()
    for index,line in enumerate(lines):
        for char in line:
            if char!='.' and not(char.isdigit()):
                symbols.add(char)
    return symbols

symbols = find_symbols(lines)

for row,line in enumerate(lines):
    number = ''
    start_index = -1
    for column, char in enumerate(line):
        if char.isdigit():
            if start_index < 0:
                start_index = column
            number += char
            if column == len(line)-1:
                number_dict = {
                    'number': int(number),
                    'row': row,
                    'column_tuple': (start_index, column-1)
                }
                numbers.append(number_dict)
                number = ''
                start_index = -1
                end_index = -1

        elif not(char.isdigit()) or column == len(line):
            end_index = column-1
            if number != '':
                # print(f'this is number{number} in row: {row} and in positions({start_index}, {end_index})')
                number_dict = {
                    'number': int(number),
                    'row': row,
                    'column_tuple': (start_index, end_index)
                }
                numbers.append(number_dict)
            number = ''
            start_index = -1
            end_index = -1

valid_numbers = []

for entry in numbers[:]:
    number = entry['number']
    start = (max(entry['row']-1, 0), max(0,entry['column_tuple'][0]-1))
    end = (min(len(lines)-1, entry['row']+1), min(len(lines[0])-1, entry['column_tuple'][1]+1))
    found = False
    for i in range(start[0], end[0]+1):
        for j in range(start[1], end[1]+1):
            # print(lines[i][j], end=' ')
            if lines[i][j] in symbols:
                valid_numbers.append((entry['number'], lines[i][j], (i, j), entry))
                found = True
        # print()
    # if found == True:
        # print(f'Found symbol: {valid_numbers[-1]}')
    # else:
        # print('NO SYMBOL FOUND')

total_sum = 0
for valid_number in valid_numbers:
    total_sum += valid_number[0]

# print(valid_numbers)
# print(total_sum)

#part 2
gear_numbers = dict()
for valid_number in valid_numbers:
    if valid_number[1]=='*':
        if valid_number[2] not in gear_numbers:
            gear_numbers[valid_number[2]] = []
        gear_numbers[valid_number[2]].append(valid_number[0])

total_sum_two = 0

for key in gear_numbers:
    if len(gear_numbers[key])==2:
        total_sum_two += gear_numbers[key][0]*gear_numbers[key][1]
print(total_sum_two)
