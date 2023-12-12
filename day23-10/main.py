import pandas as pd
from helper import read_file
import re


file_path = 'input.txt'
# file_path = 'test_input.txt'

lines = read_file(file_path = file_path)

lines = [[y for y in x] for x in lines]

def print_maze(lines):
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            print(lines[i][j], end=' ')
        print()

def find_start(lines, start_symbol = 'S'):
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == start_symbol:
                return (i,j)

def find_first_step(start_position, lines):

    if start_position[0]-1 >= 0:
        if lines[start_position[0]-1][start_position[1]] in ['|', '7', 'F']:
            return {(start_position[0]-1,start_position[1]): 'up'}

    #left
    if start_position[1]-1 >= 0:
        if lines[start_position[0]][start_position[1]-1] in ['-', 'L', 'F']:
            return {(start_position[0],start_position[1]-1):'left'}

    #down
    if start_position[0]+1 <= len(lines):
        if lines[start_position[0]+1][start_position[1]] in ['|', 'L', 'J']:
            return {(start_position[0]+1,start_position[1]): 'down'}

    #right
    if start_position[1]+1 <= len(lines[0]):
        if lines[start_position[0]][start_position[1]+1] in ['-', '7', 'J']:
            return {(start_position[0],start_position[1]+1): 'right'}


start_position = find_start(lines)
print_maze(lines)
print(start_position)

# Get the two possible next moves from the starting point (i.e. right, up, left, down)
first_step = find_first_step(start_position,lines)
print(first_step)

instructions = {
    '|': { 'down': (1,0,'down'),   'up': (-1,0,'up') },
    '-': { 'left': (0,-1,'left'),  'right': (0,1, 'right') },
    'L': { 'left': (-1,0, 'up'),  'down': (0,1, 'right') },
    'J': { 'right': (-1,0, 'up'),  'down': (0,-1, 'left') },
    '7': { 'right': (1,0, 'down'),  'up': (0,-1,'left') },
    'F': { 'left': (1,0,'down'),  'up': (0,1, 'right') }
}

step = first_step
counter = 1

while step != start_position:
    try:
        for key in step:
            direction = step[key]
            pipe = lines[key[0]][key[1]]
            temp = instructions[pipe][direction]
            lines[key[0]][key[1]] = counter
            step = {(key[0]+temp[0], key[1]+temp[1]): temp[2]}
            counter += 1
    except KeyError:
        print_maze(lines)
        break


print(f'Total number of steps: {int(counter/2)}')


