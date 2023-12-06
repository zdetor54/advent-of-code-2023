import math

import pandas as pd
from helper import read_file

file_path = 'input.txt'
# file_path = 'test_input.txt'

lines = read_file(file_path = file_path)
map_types = [(x.split()[0], index + 1) for index, x in enumerate(lines) if 'map' in x]
def get_seeds(lines):

    temp = [x for x in lines[0].split()]
    temp_seeds = temp[1:]
    temp_seeds = [int(x) for x in temp_seeds]

    seeds = []

    for i in range(math.ceil(len(temp_seeds)/2)):
        seeds.append((temp_seeds[2*i], temp_seeds[2*i+1]))

    return seeds

def get_map(lines):
    maps = dict()
    for map_type in map_types:
        maps[map_type[0]] = []
        # print(map_type[0])
        for line in lines[map_type[1]:]:

            if line != '':
                temp = dict()
                temp['destination_range_start'] = int(line.split()[0])
                temp['source_range_start'] = int(line.split()[1])
                temp['range_length'] = int(line.split()[2])
                maps[map_type[0]].append(temp)
                # print(line)
            else:
                break
    return maps

seeds = get_seeds(lines)
print(seeds)

maps = get_map(lines)
print(maps)

min_location = 10000000000000000000000

num_of_seeds = 1
for seed_group in seeds[:]:
    num_of_seeds += seed_group[1]

print(f'There are: {num_of_seeds} seeds')

total_counter = 0

for seed_group in seeds[:]:

    seed_start = seed_group[0]
    print(seed_group)
    i=0
    # for i in range(seed_group[1]):
    while i < seed_group[1]:
        total_counter+=1
        if total_counter % 1815746 == 1:
            print(f'Progress:{total_counter*100/num_of_seeds}')
        seed = seed_start+i
        lookup_value = seed
        destination_value = seed
        for map_type in map_types:
            for map in maps[map_type[0]]:
                if lookup_value in range(map['source_range_start'], map['source_range_start'] + map['range_length']):
                    destination_value = map['destination_range_start'] + lookup_value - map['source_range_start']
                    break

            lookup_value = destination_value



        if min_location > destination_value:
            min_location = destination_value
            print(f'Location for seed: {seed}({i} of {seed_group[1]}) is {destination_value}')

        i+=1

print(min_location)

