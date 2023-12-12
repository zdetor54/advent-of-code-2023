import pandas as pd
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
print(map_dictionary)


next_step = 'AAA'
# PART 1

# step = 0
# while next_step != 'ZZZ':
#     origin = next_step
#     # print(origin, end=' ')
#     next_instruction = int(instruction_string[step % len(instruction_string)])
#     # print(next_instruction)
#     next_step = map_dictionary[origin][next_instruction]
#     step +=1
# print(step)
# PART 2


def check_destinations(steps):
    all_z = True
    i=0
    while all_z == True and i<len(steps):
        if steps[i][2] != 'Z':
            all_z = False
        i+=1

    return all_z


next_steps = []
for key in map_dictionary:
    if key[2] == 'A':
        next_steps.append(key)

print(f'Possible Origins: {next_steps}')

step = 0
while check_destinations(next_steps) == False:
    if step % (100000*len(instruction_string)) == 0:
        print(f'Round: {step // len(instruction_string)}')
    origin_steps = next_steps
    next_steps = []
    # print(origin_steps)
    next_instruction = int(instruction_string[step % len(instruction_string)])
    for origin in origin_steps:
        next_step = map_dictionary[origin][next_instruction]
        # print(next_step)
        next_steps.append(next_step)
    step += 1
    # print(check_destinations(next_steps))

print(step)
