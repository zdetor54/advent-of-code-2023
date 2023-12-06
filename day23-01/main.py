import pandas as pd
from helper import read_file

file_path = 'input.txt'
# file_path = 'test_input.txt'

points = []
values = read_file(file_path = file_path)


def get_numbers_original(input_string):

    #Part1
    # numbers = {
    #     '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'
    # }
    #
    #Part2
    numbers = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8',
        'nine': '9', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'
    }

    candidate_numbers = []

    for key in numbers:
        for i in range(len(input_string)):
            if input_string.find(key, i) >= 0:
                candidate_numbers.append((numbers[key], input_string.find(key, i)))
            candidate_numbers = sorted(candidate_numbers, key=lambda x: x[1])
    # print(candidate_numbers)
    return(int(candidate_numbers[0][0]+candidate_numbers[-1][0]))
def get_numbers(input_string):

    #Part1
    # numbers = {
    #     '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'
    # }
    #
    #Part2
    numbers = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8',
        'nine': '9', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'
    }

    #Check for the first digit
    i=0
    first_digit = ''
    last_digit=''
    while i<len(input_string) and first_digit == '':
        substring = input_string[:i+1]
        for key in numbers:
            if key in substring:
                first_digit = numbers[key]
                break
        i += 1
    i = 1

    # Check for the last digit
    while i<len(input_string)+1 and last_digit == '':
        substring = input_string[-i:]
        for key in numbers:
            if key in substring:
                last_digit = numbers[key]
                break
        i += 1

    return int(first_digit+last_digit)

total = 0

for value in values[:]:
    total += get_numbers(value)

print(total)