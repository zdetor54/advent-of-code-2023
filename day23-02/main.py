import pandas as pd
from helper import read_file

file_path = 'input.txt'
# file_path = 'test_input.txt'

points = []
lines = read_file(file_path = file_path)

game_dict = dict()

for line in lines:
    temp = line.split(':')
    game = temp[0].split(" ")[1]
    game_dict[game] = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    revealed_sets = temp[1].split(';')
    for set in revealed_sets:
        draws = set.split(",")
        for draw in draws:
            temp = draw.split(' ')
            if game_dict[game][temp[2]] < int(temp[1]):
                game_dict[game][temp[2]] = int(temp[1])

print(game_dict)

expected_dict = {
        'red': 12,
        'green': 13,
        'blue': 14
}

total_sum = 0
for key in game_dict:
    possible = True

    for color in expected_dict:

        if game_dict[key][color] > expected_dict[color]:
            possible = False
            break
    if possible == True:
        total_sum += int(key)

print(total_sum)

#part 2
print(game_dict)

power_sum = 0
for game in game_dict:
    temp = 1
    for color in game_dict[game]:
        if game_dict[game][color]>0:
            temp*=game_dict[game][color]
    power_sum += temp

print(power_sum)
