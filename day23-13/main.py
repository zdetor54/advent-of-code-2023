import math

import pandas as pd
from helper import read_file
import copy

file_path = 'input.txt'
# file_path = 'test_input.txt'
lines = read_file(file_path=file_path)


def get_pattern_dictionary(lines):
    lines = [[x for x in line] for line in lines]

    pattern_num = 1
    pattern_dict = dict()
    i_start = -1
    for i in range(len(lines)):
        if len(lines[i]) == 0:
            pattern_dict[pattern_num] = lines[i_start + 1:i]
            i_start = i
            pattern_num += 1
        elif i == len(lines) - 1:
            pattern_dict[pattern_num] = lines[i_start + 1:]

        # for j in range(len(lines[i])):
        #     print(lines[i][j], end=' ')
        # print()
    return pattern_dict


pattern_dict = get_pattern_dictionary(lines)

def print_pattern(pattern):
    for i in range(len(pattern)):
        for j in range(len(pattern[i])):
            print(pattern[i][j], end=' ')
        print()



def find_horizontal_mirror(pattern, original_mirror):
    for i in range(1, len(pattern)):
        part2 = pattern[i:2 * i]
        part1 = pattern[i - len(part2):i]

        if part1 == part2[::-1] and i != original_mirror:
            return i
    return 0


def find_vertical_mirror(pattern, original_mirror):
    transposed_pattern = [[pattern[j][i] for j in range(len(pattern))] for i in
                          range(len(pattern[0]))]

    return find_horizontal_mirror(transposed_pattern, original_mirror)

def find_mirror(pattern, original_mirror=(0,0)):
    row = find_horizontal_mirror(pattern, original_mirror[0])
    column = find_vertical_mirror(pattern, original_mirror[1])
    return (row, column)



total_sum = 0


def find_smudge_mirror(pattern):
    original_mirror = find_mirror(pattern)
    for i in range(len(pattern)):
        for j in range(len(pattern[i])):
            temp = copy.deepcopy(pattern)
            if temp[i][j] == '.':
                temp[i][j] = '#'
            else:
                temp[i][j] = '.'

            temp_mirror = find_mirror(temp, original_mirror)
            if temp_mirror != original_mirror and temp_mirror != (0,0):
                print(f'{original_mirror} --> {temp_mirror}')
                return temp_mirror

for key in pattern_dict:
    print(f'This is itteration: {key}')
    pattern = pattern_dict[key]
    # temp = find_mirror(pattern) # Swap with the line below for part 1
    temp = find_smudge_mirror(pattern)
    total_sum += temp[0]*100 + temp[1]

print(total_sum)
