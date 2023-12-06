import pandas as pd
from helper import read_file

file_path = 'input.txt'
# file_path = 'test_input.txt'

lines = read_file(file_path = file_path)

maps_types = [(x.split()[0], index+1) for index, x in enumerate(lines) if 'map' in x]

def get_seeds(input):

    temp = [x for x in lines[0].split()]
    seeds = temp[1:]

    seed_dict = dict()
    for index, seed in enumerate(seeds):
        seed_dict[index] = {'seed': int(seed)}

    return seed_dict


seed_list = get_seeds(lines)


maps = dict()
for map_type in maps_types:
    maps[map_type[0]] = []
    # print(map_type[0])
    for line in lines[map_type[1]:]:

        if line!='':
            temp = dict()
            temp['destination_range_start'] = int(line.split()[0])
            temp['source_range_start'] = int(line.split()[1])
            temp['range_length'] = int(line.split()[2])
            maps[map_type[0]].append(temp)
            # print(line)
        else:
            break
print(maps)
# PART 1

for map_type in maps_types:
    # print(seed_list)
    source = map_type[0].split('-')[0]
    destination = map_type[0].split('-')[2]

    for element in seed_list:
        lookup_value = seed_list[element][source]
        destination_value = lookup_value
        for map in maps[map_type[0]]:
            if lookup_value in range (map['source_range_start'],map['source_range_start']+map['range_length']):
                destination_value = map['destination_range_start']+lookup_value - map['source_range_start']
            seed_list[element][destination] = destination_value


min_location = 100000000000000
for element in seed_list:
    if seed_list[element]['location']<min_location:
        min_location = seed_list[element]['location']

print(min_location)
print(seed_list)

# PART 2

