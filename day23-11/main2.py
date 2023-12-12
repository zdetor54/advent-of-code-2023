import pandas as pd
from helper import read_file
import re


file_path = 'input.txt'
# file_path = 'test_input.txt'

lines = read_file(file_path = file_path)

lines = [[y for y in x] for x in lines]

def print_space(lines):
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            print(lines[i][j], end=' ')
        print()

def manhattan_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return abs(x1 - x2) + abs(y1 - y2)


galaxies_dict = dict()
galaxy = 1
empty_rows = [x for x in range(len(lines))]
empty_columns = [x for x in range(len(lines[0]))]

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == '#':
            galaxies_dict[galaxy] = (i,j)
            try:
                empty_rows.remove(i)
            except ValueError:
                pass
            try:
                empty_columns.remove(j)
            except ValueError:
                pass
            galaxy += 1
print(galaxies_dict)
print(empty_rows)
print(empty_columns)

expansion_parameter = 1000000-1

for index,element in enumerate(empty_rows):

    empty_rows[index+1:] = [x+expansion_parameter for x in empty_rows[index+1:]]
    for key in galaxies_dict:
        if galaxies_dict[key][0] > element:
            galaxies_dict[key] = (galaxies_dict[key][0]+expansion_parameter, galaxies_dict[key][1])

for index,element in enumerate(empty_columns):
    empty_columns[index + 1:] = [x + expansion_parameter for x in empty_columns[index + 1:]]
    for key in galaxies_dict:
        if galaxies_dict[key][1] > element:
            galaxies_dict[key] = (galaxies_dict[key][0], galaxies_dict[key][1]+expansion_parameter)

print(galaxies_dict)
galaxies_list = list(galaxies_dict.keys())

print(galaxies_list)

galaxies_pairs_list = []

for i in range(len(galaxies_list)):
    for j in range(i+1,len(galaxies_list)):
        galaxies_pairs_list.append((galaxies_list[i], galaxies_list[j]))

total_distance = 0
for pair in galaxies_pairs_list:
    point_a = galaxies_dict[pair[0]]
    point_b = galaxies_dict[pair[1]]
    distance = manhattan_distance(point_a, point_b)
    total_distance += distance

print(f'The total distance is: {total_distance}')


# print_space(lines)
