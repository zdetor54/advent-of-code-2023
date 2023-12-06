import pandas as pd
from helper import read_file

file_path = 'input.txt'
# file_path = 'test_input.txt'

points = []
lines = read_file(file_path = file_path)
lines = [x.split(':')[1] for x in lines]

lines = [(x.split('|')[0], x.split('|')[1]) for x in lines]

# PART 1
matches = []
for line in lines:
    print(line)
    winning_numbers = line[0].split()
    your_numbers = line[1].split()
    intersection_list = [x for x in winning_numbers if x in your_numbers]
    matches.append(intersection_list)
    # print(intersection_list)

total = 0
for match in matches:
    if len(match)>0:
        total += 2**(len(match)-1)

print(total)

# PART 2

scores = dict()
for i in range(len(matches)):
    scores[i+1] = dict()
    scores[i+1]['matches'] = len(matches[i])
    scores[i+1]['copies'] = 1


for card_number in scores:
    for i in range(scores[card_number]['matches']):
        scores[card_number+i+1]['copies'] += scores[card_number]['copies']

new_total = 0

for card in scores:
    new_total+=scores[card]['copies']

print(new_total)