import pandas as pd
from helper import read_file

# file_path = 'input.txt'
file_path = 'test_input.txt'

points = []
formations = read_file(file_path = file_path)
for formation in formations:
    temp = [(int(x.split(',')[0]), int(x.split(',')[1])) for x in formation.split(' -> ')]
    points.append(temp)
def initialise_grid (points, source):
    min_width = 1000000
    max_width = 0
    max_depth = 0
    for segment in points:
        for point in segment:
            if point[0] < min_width:
                min_width = point[0]
            if point[0] > max_width:
                max_width = point[0]
            if point[1] > max_depth:
                max_depth = point[1]

    print ((min_width,max_width, max_depth))

    patern = ['']
    for j in range(max_width):
        if j == source[0]-1:
            patern[0] += ('+')
        else:
            patern[0] += ('.')

    for i in range(1, max_depth+2):
        patern.append([])
        for j in range(max_width):
            patern[i].append('.')
    return patern

patern = initialise_grid(points, source = (500,0))

def print_patern(patern):
    for i in range(len(patern)):
        print(i, end=' ')
        for j in range(492, len(patern[i])):
            print(patern[i][j], end=' ')
        print()

print_patern(patern)

def add_segments(segments, patern):
    print(segments)
    for i in range(len(segments)-1):
        starting_point = segments[i]
        ending_point = segments[i+1]
        print(starting_point, ending_point)
        if starting_point[0] == ending_point[0]: #vertical move
            for i in range( min(starting_point[1],ending_point[1]),max(starting_point[1],ending_point[1])+1):
                patern[i][starting_point[0]-1] = "#"
        else:
            for j in range( min(starting_point[0],ending_point[0])-1 ,max(starting_point[0],ending_point[0])):
                patern[starting_point[1]][j] = "#"
        print_patern(patern)
        print()

for segments in points:
    add_segments(segments, patern)
    print_patern(patern)
