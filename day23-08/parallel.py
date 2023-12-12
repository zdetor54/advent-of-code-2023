import copy
from helper import read_file
import re


file_path = 'input.txt'
# file_path = 'test_input.txt'

lines = read_file(file_path = file_path)

#Get the left right instructions
instruction_string = lines[0].replace('R','1').replace('L','0')
print(f'Get the left right instructions: {instruction_string}')

#Get the map
pattern = re.compile('[( )]')
map_dictionary = {x.split('=')[0].strip(): (pattern.sub('', x.split('=')[1].strip()).split(',')[0], pattern.sub('', x.split('=')[1].strip()).split(',')[1]) for x in lines[2:]}
for key in map_dictionary:
    temp = map_dictionary[key]
    map_dictionary[key] = dict()

    map_dictionary[key][0] = temp[0]
    map_dictionary[key][1] = temp[1]
print(map_dictionary)


def find_nodes(match):
    nodes = []
    for key in map_dictionary:
        if key[2] == match:
            nodes.append(key)

    return nodes

origin_points = find_nodes('A')
destination_points = find_nodes('Z')

print(f'Origins: {origin_points}')
print(f'Destinations: {destination_points}')

def find_path(origin, destination):
    past_moves = dict()
    step = 0
    next_step = origin
    while next_step != destination:
        origin = next_step
        next_instruction = int(instruction_string[step % len(instruction_string)])
        next_step = map_dictionary[origin][next_instruction]
        if step % len(instruction_string) not in past_moves:
            past_moves[step % len(instruction_string)] = [next_step]
        elif next_step not in past_moves[step % len(instruction_string)]:
            past_moves[step % len(instruction_string)].append(next_step)
        else:
            step = -1000000000000000000000000000001
            next_step = destination
        step += 1
    return step

numbers_list = []

for origin in origin_points[:]:
    step = 0
    for destination in destination_points[:]:
        step = find_path(origin,destination)
        if step>0:
            numbers_list.append(step)

# PART 2



import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def lcm_of_list(numbers):
    result = 1
    for num in numbers:
        result = lcm(result, num)
    return result


result_list = lcm_of_list(numbers_list)

print(f"LCM of {numbers_list} is {result_list}")