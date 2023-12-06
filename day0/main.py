import pandas as pd
from helper import read_file

file_path = 'input.txt'
# file_path = 'test_input.txt'

calories = read_file(file_path = file_path)

total_calories = []
temp_cal = 0

for calorie in calories:

    if calorie != '':
        temp_cal+=int(calorie)
    else:
        total_calories.append(temp_cal)
        temp_cal = 0

total_calories.sort(reverse=True)

print(total_calories)
print(sum(total_calories[:3]))